# Generated by Django 2.0.4 on 2018-06-30 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20180628_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumsection',
            name='section_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
