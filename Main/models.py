from django.db import models


class Collections(models.Model):
    name = models.CharField(max_length=127, primary_key=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Shape(models.Model):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    door_type = models.CharField(max_length=127)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    bevel = models.CharField(max_length=127, null=True, blank=True)
    image = models.ImageField(upload_to='Shape/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Shape/', verbose_name='icon')
    Grid_image = models.ImageField(upload_to='Grid/', verbose_name='Grid Photo', null=True, blank=True)
    Grid_icon = models.ImageField(upload_to='icon/Grid/', verbose_name='Grid Icon', null=True, blank=True)
    Bevel_icon = models.ImageField(upload_to='icon/Bevel/', verbose_name='Bevel icon', null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['collections'])
        ]


class Decore(models.Model):
    name = models.CharField(max_length=127, primary_key=True)
    price = models.FloatField()

    class Meta:
        abstract = True


class Portal(Decore):
    image = models.ImageField(upload_to='Portal/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Portal/', verbose_name='icon')


class Molding(Decore):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Molding/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Molding/', verbose_name='icon')

    class Meta:
        indexes = [
            models.Index(fields=['collections'])
        ]


class Carnice(Decore):
    image = models.ImageField(upload_to='Carnice/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Carnice/', verbose_name='icon')


class Podium(Decore):
    image = models.ImageField(upload_to='Podium/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Podium/', verbose_name='icon')


class Socket(Decore):
    image = models.ImageField(upload_to='Socket/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Socket/', verbose_name='icon')


class Boots(Decore):
    image = models.ImageField(upload_to='Boots/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Boots/', verbose_name='icon')


class UniqueKey(models.Model):
    key = models.CharField(max_length=108, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    Key = models.CharField(max_length=128, null=True, blank=True)
    shape = models.CharField(max_length=128, null=True, blank=True)
    type = models.CharField(max_length=128, null=True, blank=True)
    bevel = models.CharField(max_length=128, null=True, blank=True)
    grid = models.CharField(max_length=128, null=True, blank=True)
    grid_bevel = models.CharField(max_length=128, null=True, blank=True)
    molding = models.CharField(max_length=64, null=True, blank=True)
    molding_color = models.CharField(max_length=64, null=True, blank=True)
    portal = models.CharField(max_length=64, null=True, blank=True)
    image = models.CharField(max_length=64, null=True, blank=True)
    icon = models.CharField(max_length=64, null=True, blank=True)
    carnice = models.CharField(max_length=64, null=True, blank=True)
    podium = models.CharField(max_length=64, null=True, blank=True)
    socket = models.CharField(max_length=64, null=True, blank=True)
    boots = models.CharField(max_length=64, null=True, blank=True)
    color = models.CharField(max_length=64, null=True, blank=True)
    door_price = models.FloatField()
    size = models.CharField(max_length=16)
    quantity = models.PositiveIntegerField(default=1)


class Shpone(models.Model):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    door_type = models.CharField(max_length=127)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    color = models.CharField(max_length=127)
    portal = models.CharField(max_length=127)
    portal_image = models.ImageField(upload_to='Portals/')
    image = models.ImageField(upload_to='Shape/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Shape/', verbose_name='icon')

    class Meta:
        indexes = [
            models.Index(fields=['collections'])
        ]


class Shpon_Carnice(Decore):
    image = models.ImageField(upload_to='Carnice/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Carnice/', verbose_name='icon')
    color = models.CharField(max_length=127)


class Shpon_Socket(Decore):
    image = models.ImageField(upload_to='Socket/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Socket/', verbose_name='icon')
    color = models.CharField(max_length=127)


class Shpon_Boots(Decore):
    image = models.ImageField(upload_to='Boots/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Boots/', verbose_name='icon')
    color = models.CharField(max_length=127)


class Shpon_Molding(Decore):
    collections = models.ForeignKey(Collections, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Molding/', verbose_name='Photo')
    icon = models.ImageField(upload_to='icon/Molding/', verbose_name='icon')
    color = models.CharField(max_length=127)

    class Meta:
        indexes = [
            models.Index(fields=['collections'])
        ]
