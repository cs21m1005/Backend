# Generated by Django 4.0.4 on 2022-07-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_shipping_delete_cartitem_remove_purchase_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Mobile_Number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='MRP',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Pricing',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Quantity',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='Pincode',
            field=models.CharField(max_length=6),
        ),
    ]
