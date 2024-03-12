# Generated by Django 5.0.3 on 2024-03-11 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0011_remove_trip_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='connected_users',
        ),
        migrations.AddField(
            model_name='trip',
            name='connected_users',
            field=models.ManyToManyField(related_name='user_connected_trips', to=settings.AUTH_USER_MODEL),
        ),
    ]
