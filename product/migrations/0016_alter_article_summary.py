# Generated by Django 3.2 on 2021-08-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20210829_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(),
        ),
    ]
