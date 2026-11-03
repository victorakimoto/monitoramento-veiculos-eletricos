from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Veiculo, Lancamento
from .serializers import (
    RegistroUsuarioSerializer,
    VeiculoSerializer,
    LancamentoSerializer,
    EficienciaVeiculoSerializer,
)


class RegistroUsuarioView(generics.CreateAPIView):
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [permissions.AllowAny]


class VeiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class LancamentoViewSet(viewsets.ModelViewSet):
    serializer_class = LancamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Lancamento.objects.filter(veiculo__usuario=self.request.user)
        veiculo_id = self.request.query_params.get('veiculo')
        if veiculo_id:
            qs = qs.filter(veiculo_id=veiculo_id)
        return qs

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ComparadorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        veiculos = (
            Veiculo.objects
            .filter(usuario=request.user)
            .annotate(
                km_total=Sum('lancamentos__quilometragem_rodada'),
                kwh_total=Sum(
                    ExpressionWrapper(
                        (100 - F('lancamentos__nivel_bateria_percentual')) / 100
                        * F('capacidade_bateria_kwh'),
                        output_field=DecimalField(max_digits=12, decimal_places=4),
                    )
                ),
            )
        )
        dados = []
        for v in veiculos:
            km_por_kwh = None
            if v.km_total and v.kwh_total:
                km_por_kwh = round(v.km_total / v.kwh_total, 2)
            dados.append({
                'veiculo_id': v.id, 'marca': v.marca, 'modelo': v.modelo,
                'ano': v.ano, 'km_total': v.km_total or 0, 'km_por_kwh': km_por_kwh,
            })
        serializer = EficienciaVeiculoSerializer(dados, many=True)
        return Response(serializer.data)
    # ADICIONAR ao final de veiculos/views.py
# (imports extras: from django.db import transaction
#                  from rest_framework.decorators import action
#                  from rest_framework.exceptions import ValidationError
#                  from .models import VeiculoCatalogo, Compra
#                  from .serializers import VeiculoCatalogoSerializer, CompraSerializer)
from django.db import transaction
from rest_framework import mixins, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Veiculo, VeiculoCatalogo, Compra
from .serializers import VeiculoCatalogoSerializer, CompraSerializer


class CatalogoViewSet(viewsets.ReadOnlyModelViewSet):
    """Vitrine pública: GET /api/catalogo/ e /api/catalogo/<id>/ (cadastro pelo admin)."""
    serializer_class = VeiculoCatalogoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return VeiculoCatalogo.objects.filter(ativo=True)


class CompraViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """POST /api/compras/ {veiculo_catalogo, forma_pagamento}; GET lista as compras do usuário."""
    serializer_class = CompraSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Compra.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        with transaction.atomic():
            # trava a linha para dois compradores não levarem a última unidade
            item = VeiculoCatalogo.objects.select_for_update().get(
                pk=serializer.validated_data['veiculo_catalogo'].pk)
            if not item.ativo or item.estoque < 1:
                raise ValidationError('Veículo indisponível no estoque.')
            item.estoque -= 1
            item.save(update_fields=['estoque'])
            # o veículo comprado entra na garagem, pronto para monitorar e comparar
            garagem = Veiculo.objects.create(
                usuario=self.request.user, marca=item.marca, modelo=item.modelo,
                ano=item.ano, capacidade_bateria_kwh=item.capacidade_bateria_kwh)
            serializer.save(usuario=self.request.user, veiculo=garagem, preco_pago=item.preco)

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        with transaction.atomic():
            compra = self.get_object()
            if compra.status == 'CANCELADA':
                raise ValidationError('Compra já cancelada.')
            garagem = compra.veiculo
            if garagem and garagem.lancamentos.exists():
                raise ValidationError('Não é possível cancelar: o veículo já tem lançamentos.')
            item = VeiculoCatalogo.objects.select_for_update().get(pk=compra.veiculo_catalogo_id)
            item.estoque += 1
            item.save(update_fields=['estoque'])
            compra.status = 'CANCELADA'
            compra.veiculo = None
            compra.save()
            if garagem:
                garagem.delete()
        return Response(self.get_serializer(compra).data)