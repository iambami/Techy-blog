# Generated by Django 3.1 on 2020-08-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200818_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='snippet',
            field=models.CharField(default='Click Link above to read full Story', max_length=255),
        ),
    ]
