from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Veiculo, Lancamento


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'marca', 'modelo', 'ano', 'capacidade_bateria_kwh', 'criado_em']
        read_only_fields = ['id', 'criado_em']


class LancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lancamento
        fields = [
            'id', 'veiculo', 'data_lancamento',
            'quilometragem_rodada', 'nivel_bateria_percentual',
            'criado_em', 'atualizado_em',
        ]
        read_only_fields = ['id', 'data_lancamento', 'criado_em', 'atualizado_em']

    def validate_veiculo(self, veiculo):
        request = self.context['request']
        if veiculo.usuario_id != request.user.id:
            raise serializers.ValidationError('Este veículo não pertence a você.')
        return veiculo


class EficienciaVeiculoSerializer(serializers.Serializer):
    veiculo_id = serializers.IntegerField()
    marca = serializers.CharField()
    modelo = serializers.CharField()
    ano = serializers.IntegerField()
    km_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    km_por_kwh = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)