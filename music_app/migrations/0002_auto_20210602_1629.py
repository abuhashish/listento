# Generated by Django 2.2.4 on 2021-06-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='star',
            field=models.IntegerField(),
        ),
    ]
