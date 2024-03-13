# Generated by Django 5.0.1 on 2024-03-13 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_alter_venta_precio_venta_alter_venta_total_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000000),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(decimal_places=2, max_digits=10000000),
        ),
    ]
