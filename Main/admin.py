from django.contrib import admin
from .models import (
    Collections, Shape, Portal, Molding, Carnice, Podium, Socket, Boots,
    UniqueKey, CartItem, Shpone, Shpon_Carnice, Shpon_Socket, Shpon_Boots, Shpon_Molding
)

@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name', 'collections', 'door_type', 'price', 'bevel')
    list_filter = ('collections', 'door_type')
    search_fields = ('name', 'collections__name', 'door_type')

@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Molding)
class MoldingAdmin(admin.ModelAdmin):
    list_display = ('name', 'collections', 'price')
    list_filter = ('collections',)
    search_fields = ('name', 'collections__name')

@admin.register(Carnice)
class CarniceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Podium)
class PodiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Boots)
class BootsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(UniqueKey)
class UniqueKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'created_at')
    search_fields = ('key',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('Key', 'shape', 'door_price', 'size', 'quantity')
    list_filter = ('shape',)
    search_fields = ('Key', 'shape')

@admin.register(Shpone)
class ShponeAdmin(admin.ModelAdmin):
    list_display = ('name', 'collections', 'door_type', 'price', 'color', 'portal')
    list_filter = ('collections', 'door_type', 'color')
    search_fields = ('name', 'collections__name', 'door_type', 'color', 'portal')

@admin.register(Shpon_Carnice)
class ShponCarniceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'color')

@admin.register(Shpon_Socket)
class ShponSocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'color')

@admin.register(Shpon_Boots)
class ShponBootsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'color')

@admin.register(Shpon_Molding)
class ShponMoldingAdmin(admin.ModelAdmin):
    list_display = ('name', 'collections', 'price', 'color')
    list_filter = ('collections', 'color')
    search_fields = ('name', 'collections__name', 'color')
