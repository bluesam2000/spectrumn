# Generated by Django 2.2 on 2020-09-27 09:12

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_food', '0008_auto_20200927_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 27, 9, 12, 1, 580036, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='posts_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='posts_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
