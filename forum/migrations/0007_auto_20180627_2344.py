# Generated by Django 2.0.4 on 2018-06-27 17:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_auto_20180620_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumsection',
            name='admin',
        ),
        migrations.AddField(
            model_name='forumsection',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
