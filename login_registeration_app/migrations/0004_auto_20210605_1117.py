# Generated by Django 2.2.4 on 2021-06-05 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registeration_app', '0003_auto_20210605_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='following',
            new_name='followeduser',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='followers',
            new_name='followinguser',
        ),
    ]
