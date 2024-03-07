# Generated by Django 5.0.2 on 2024-03-04 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_alter_venta_fecha_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
