# Generated by Django 5.1.2 on 2024-11-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(related_name='following', through='profiles.Follow', to='profiles.userprofile'),
        ),
    ]
