# Generated by Django 3.0.6 on 2020-06-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_bot', '0006_auto_20200603_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='vk_sender',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
