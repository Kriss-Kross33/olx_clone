# Generated by Django 3.1.2 on 2020-10-24 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
