# Generated by Django 3.1 on 2020-08-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20200820_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='artPix',
            field=models.ImageField(blank=True, default='img.jpeg', null=True, upload_to='images'),
        ),
    ]
