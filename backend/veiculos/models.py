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
# ============================================================
# ADICIONAR ao final de veiculos/models.py (concessionária virtual)
# ============================================================
from django.contrib.auth.models import User
from django.db import models


class VeiculoCatalogo(models.Model):
    """Veículo à venda na concessionária virtual (cadastrado pelo admin)."""
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    ano = models.IntegerField()
    capacidade_bateria_kwh = models.DecimalField(max_digits=6, decimal_places=2)
    preco = models.DecimalField(max_digits=12, decimal_places=2)  # preço simulado
    estoque = models.PositiveIntegerField(default=1)
    imagem_url = models.URLField(blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['marca', 'modelo']

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano})'


class Compra(models.Model):
    FORMAS = [('A_VISTA', 'À vista'), ('FINANCIADO', 'Financiado')]
    STATUS = [('CONFIRMADA', 'Confirmada'), ('CANCELADA', 'Cancelada')]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    veiculo_catalogo = models.ForeignKey(VeiculoCatalogo, on_delete=models.PROTECT, related_name='compras')
    # veículo criado na garagem do usuário ao comprar (para monitorar/comparar)
    veiculo = models.OneToOneField('Veiculo', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='compra')
    preco_pago = models.DecimalField(max_digits=12, decimal_places=2)  # preço no momento da compra
    forma_pagamento = models.CharField(max_length=12, choices=FORMAS, default='A_VISTA')
    status = models.CharField(max_length=12, choices=STATUS, default='CONFIRMADA')
    data_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_compra']

    def __str__(self):
        return f'{self.usuario} comprou {self.veiculo_catalogo} ({self.status})'