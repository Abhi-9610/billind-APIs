# Generated by Django 5.0 on 2024-04-07 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0006_product_quantity_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.customer'),
        ),
    ]
