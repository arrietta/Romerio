from uuid import uuid4

from django.db import models


class Collections(models.Model):
    name = models.CharField(max_length=127, primary_key=True)
    type = models.CharField(max_length=127)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Product(models.Model):
    name = models.CharField(max_length=127, primary_key=True)
    price = models.FloatField()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['name'])
        ]


class Portal(Product):
    image = models.ImageField(upload_to='Portal/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Portal/', verbose_name='Изображение', default="none.png")


class Carnice(Product):
    image = models.ImageField(upload_to='Carnice/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Carnice/', verbose_name='Изображение', default="none.png")


class Podium(Product):
    image = models.ImageField(upload_to='Podium/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Podium/', verbose_name='Изображение', default="none.png")


class Socket(Product):
    image = models.ImageField(upload_to='Socket/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Socket/', verbose_name='Изображение', default="none.png")


class Boots(Product):
    image = models.ImageField(upload_to='Boots/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Boots/', verbose_name='Изображение', default="none.png")


class BaseDoor(models.Model):
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    door_type = models.CharField(max_length=127)
    door_image = models.ImageField(upload_to='Door/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Door/', verbose_name='Изображение', default="none.png")
    shape = models.CharField(max_length=127)
    shape_price = models.FloatField()
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    carnice = models.ForeignKey(Carnice, on_delete=models.CASCADE)
    podium = models.ForeignKey(Podium, on_delete=models.CASCADE)
    socket = models.ForeignKey(Socket, on_delete=models.CASCADE)
    boots = models.ForeignKey(Boots, on_delete=models.CASCADE)
    door_price = models.FloatField()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['collection'])
        ]

    def save(self, *args, **kwargs):
        self.door_price = (self.portal.price + self.carnice.price + self.podium.price +
                           self.socket.price + self.boots.price + self.shape_price)
        super().save(*args, **kwargs)


class Doors(BaseDoor):
    pass


class ClassicDoor(BaseDoor):
    Bevel = models.CharField(max_length=127)
    icon = models.ImageField(upload_to='icon/Bevel/', verbose_name='Изображение', default="none.png")


class ClassicBaguette(BaseDoor):
    Molding = models.CharField(max_length=127)
    Molding_image = models.ImageField(upload_to='Molding/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Molding/', verbose_name='Изображение', default="none.png")


class GrigliaDoor(BaseDoor):
    Grid = models.CharField(max_length=127)
    Grid_image = models.ImageField(upload_to='Grid/', verbose_name='Изображение')
    icon = models.ImageField(upload_to='icon/Grid/', verbose_name='Изображение', default="none.png")
    Bevel_icon = models.ImageField(upload_to='icon/Bevel/', verbose_name='Изображение' , default="none.png")
    Bevel = models.CharField(max_length=127)


class Cart(models.Model):
    user_token = models.UUIDField(default=uuid4, editable=False, unique=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    base_door = models.ForeignKey(Doors, on_delete=models.CASCADE, null=True, blank=True)
    classic_door = models.ForeignKey(ClassicDoor, on_delete=models.CASCADE, null=True, blank=True)
    classic_baguette = models.ForeignKey(ClassicBaguette, on_delete=models.CASCADE, null=True, blank=True)
    griglia_door = models.ForeignKey(GrigliaDoor, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
