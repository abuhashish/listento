# Generated by Django 2.2.4 on 2021-06-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_remove_music_music'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
