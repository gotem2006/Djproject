# Generated by Django 4.2.6 on 2023-11-14 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_quntity_basket_qauntity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAtribute',
            new_name='ProductAttribute',
        ),
    ]