# Generated by Django 4.2.3 on 2023-07-24 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0004_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('number_phone', models.CharField(max_length=11, verbose_name='Number Phone')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('date_and_creation', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(through='online_shop.ItemInCart', to='online_shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='itemincart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_shop.order'),
        ),
        migrations.AddField(
            model_name='itemincart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_shop.product'),
        ),
    ]
