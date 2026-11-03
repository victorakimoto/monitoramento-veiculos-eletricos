from django.contrib import admin
from .models import Veiculo, Lancamento

admin.site.register(Veiculo)
admin.site.register(Lancamento)
# veiculos/admin.py — adicionar:
from django.contrib import admin
from .models import VeiculoCatalogo, Compra
admin.site.register(VeiculoCatalogo)
admin.site.register(Compra)