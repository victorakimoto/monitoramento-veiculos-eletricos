from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Veiculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='veiculos')
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    ano = models.IntegerField()
    capacidade_bateria_kwh = models.DecimalField(max_digits=6, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'


class Lancamento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='lancamentos')
    data_lancamento = models.DateField(auto_now_add=True)
    quilometragem_rodada = models.DecimalField(max_digits=8, decimal_places=2)
    nivel_bateria_percentual = models.DecimalField(max_digits=5, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data_lancamento']

    def __str__(self):
        return f'{self.veiculo} — {self.data_lancamento}'
