# Generated by Django 3.0.4 on 2020-04-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_default.png', upload_to='products_pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(max_length=1),
        ),
    ]
