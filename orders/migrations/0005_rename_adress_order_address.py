# Generated by Django 4.2.6 on 2024-01-09 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
    ]
