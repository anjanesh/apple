# Generated by Django 3.2 on 2021-05-14 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210514_1336'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsByReseller',
            new_name='Item',
        ),
    ]
