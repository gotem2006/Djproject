# Generated by Django 4.2.6 on 2023-11-09 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_basket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='quntity',
            new_name='qauntity',
        ),
    ]
