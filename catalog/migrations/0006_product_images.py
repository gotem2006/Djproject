# Generated by Django 4.2.6 on 2023-11-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_productatribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(null=True, upload_to='product_images/%Y-%m-%d/', verbose_name='Фотографии товара'),
        ),
    ]
