# Generated by Django 3.1.1 on 2020-12-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201208_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]