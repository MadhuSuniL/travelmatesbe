# Generated by Django 5.0.3 on 2024-03-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0009_triplike_dis_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triplike',
            name='dis_like',
        ),
        migrations.AddField(
            model_name='triplike',
            name='status',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike')], default='like', max_length=10),
        ),
    ]
