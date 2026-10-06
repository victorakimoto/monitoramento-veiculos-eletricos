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