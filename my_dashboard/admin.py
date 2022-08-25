from django.contrib import admin
from .models import Produto, Vendas, Vendedor


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome']
   
    
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    

@admin.register(Vendas)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'vendedor', 'total', 'data']