# Generated by Django 3.2.13 on 2022-07-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_rename_servicecenters_servicecenter'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='offers',
            field=models.TextField(blank=True, null=True),
        ),
    ]