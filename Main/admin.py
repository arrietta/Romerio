from django.contrib import admin
from .models import Collections, Portal, Carnice, Podium, Socket, Boots, Doors, ClassicDoor, ClassicBaguette, GrigliaDoor, Cart, CartItem

# Регистрация моделей в административной панели
admin.site.register(Collections)
admin.site.register(Portal)
admin.site.register(Carnice)
admin.site.register(Podium)
admin.site.register(Socket)
admin.site.register(Boots)
admin.site.register(Doors)
admin.site.register(ClassicDoor)
admin.site.register(ClassicBaguette)
admin.site.register(GrigliaDoor)
admin.site.register(Cart)
admin.site.register(CartItem)
