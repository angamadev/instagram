# Generated by Django 5.1.2 on 2024-11-07 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_follow_userprofile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
    ]
