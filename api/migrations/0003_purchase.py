# Generated by Django 4.0.4 on 2022-07-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=200)),
                ('Quantity', models.CharField(max_length=200)),
                ('Pricing', models.CharField(max_length=200)),
                ('MRP', models.CharField(max_length=200)),
            ],
        ),
    ]
