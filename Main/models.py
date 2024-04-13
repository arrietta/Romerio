from uuid import uuid4

from django.db import models


class Collections(models.Model):
    name = models.CharField(max_length=127, primary_key=True)
    type = models.CharField(max_length=127)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Shape(models.Model):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    door_type = models.CharField(max_length=127)
    name = models.CharField(max_length=127, primary_key=True)

    price = models.FloatField()
    image = models.ImageField(upload_to='Shape/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Shape/', verbose_name='icon')
    Grid_image = models.ImageField(upload_to='Grid/', verbose_name='Grid Photo', default="none.png")
    Grid_icon = models.ImageField(upload_to='icon/Grid/', verbose_name='Grid Icon', default="none.png")
    Bevel_icon = models.ImageField(upload_to='icon/Bevel/', verbose_name='Bevel icon', default="none.png")


    class Meta:
        indexes = [
            models.Index(fields=['collections'])
        ]


class Product(models.Model):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    name = models.CharField(max_length=127, primary_key=True)
    price = models.FloatField()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['collections'])
        ]


class Portal(Product):
    image = models.ImageField(upload_to='Portal/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Portal/', verbose_name='icon')


class Molding(Product):
    image = models.ImageField(upload_to='Molding/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Molding/', verbose_name='icon')


class Carnice(Product):
    image = models.ImageField(upload_to='Carnice/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Carnice/', verbose_name='icon')


class Podium(Product):
    image = models.ImageField(upload_to='Podium/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Podium/', verbose_name='icon')


class Socket(Product):
    image = models.ImageField(upload_to='Socket/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Socket/', verbose_name='icon')


class Boots(Product):
    image = models.ImageField(upload_to='Boots/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Boots/', verbose_name='icon')


# class BaseDoor(models.Model):
#     collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
#     door_type = models.CharField(max_length=127)
#     door_image = models.ImageField(upload_to='Door/', verbose_name='Изображение')
#     icon = models.ImageField(upload_to='icon/Door/', verbose_name='Изображение', default="none.png")
#     shape = models.CharField(max_length=127)
#     shape_price = models.FloatField()
#     portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
#     carnice = models.ForeignKey(Carnice, on_delete=models.CASCADE)
#     podium = models.ForeignKey(Podium, on_delete=models.CASCADE)
#     socket = models.ForeignKey(Socket, on_delete=models.CASCADE)
#     boots = models.ForeignKey(Boots, on_delete=models.CASCADE)
#     door_price = models.FloatField()

# class Meta:
#     abstract = True
#     indexes = [
#         models.Index(fields=['collection'])
#     ]

# def save(self, *args, **kwargs):
#     self.door_price = (self.portal.price + self.carnice.price + self.podium.price +
#                        self.socket.price + self.boots.price + self.shape_price)
#     super().save(*args, **kwargs)


class Cart(models.Model):
    user_token = models.UUIDField(default=uuid4, editable=False, unique=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    molding = models.ForeignKey(Molding, on_delete=models.CASCADE)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    carnice = models.ForeignKey(Carnice, on_delete=models.CASCADE)
    podium = models.ForeignKey(Podium, on_delete=models.CASCADE)
    socket = models.ForeignKey(Socket, on_delete=models.CASCADE)
    boots = models.ForeignKey(Boots, on_delete=models.CASCADE)
    door_price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
