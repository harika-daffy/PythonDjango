# Generated by Django 3.0.8 on 2020-07-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feild',
            field=models.BooleanField(default=True),
        ),
    ]
