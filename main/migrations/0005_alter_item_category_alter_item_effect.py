# Generated by Django 4.2.5 on 2023-09-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_product_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='effect',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
