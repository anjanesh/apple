# Generated by Django 3.2 on 2021-05-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_productsbyreseller_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-last_updated']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='item',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
