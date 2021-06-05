# Generated by Django 2.2.4 on 2021-06-05 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registeration_app', '0004_auto_20210605_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=45)),
                ('writer', models.CharField(max_length=45)),
                ('composer', models.CharField(max_length=45)),
                ('duration', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lyrics', models.TextField()),
                ('music', models.FileField(blank=True, upload_to='audio/')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='login_registeration_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rates', to='music_app.Music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rates', to='login_registeration_app.User')),
            ],
        ),
    ]
