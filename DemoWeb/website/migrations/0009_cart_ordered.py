# Generated by Django 4.2.4 on 2023-08-24 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_cart_cartproduct_delete_user_cart_products_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]