# Generated by Django 3.1.2 on 2020-10-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product/'),
        ),
    ]
