# Generated by Django 4.2.7 on 2024-06-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_cartitem_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='grid',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
