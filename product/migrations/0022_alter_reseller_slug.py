# Generated by Django 3.2.10 on 2021-12-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_reseller_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseller',
            name='slug',
            field=models.SlugField(),
        ),
    ]
