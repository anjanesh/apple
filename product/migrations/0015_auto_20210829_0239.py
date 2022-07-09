# Generated by Django 3.2 on 2021-08-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_article_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
