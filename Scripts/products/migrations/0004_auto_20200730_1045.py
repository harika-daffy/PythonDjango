# Generated by Django 3.0.8 on 2020-07-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200730_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feild',
            field=models.BooleanField(default=True),
        ),
    ]
