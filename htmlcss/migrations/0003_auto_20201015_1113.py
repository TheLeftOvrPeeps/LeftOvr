# Generated by Django 3.1.2 on 2020-10-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0002_auto_20201015_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='idNum',
            field=models.CharField(max_length=13),
        ),
    ]