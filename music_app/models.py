from django.db import models
from login_registeration_app.models import User
# Create your models here.
class Music(models.Model):
    song_name=models.CharField(max_length=45)
    writer=models.CharField(max_length=45)
    composer = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lyrics=models.TextField()
    uploaded_by=models.ForeignKey(User,related_name="songs",on_delete=models.CASCADE)
    
class Star(models.Model):
    star=models.IntegerField(max_length=5)
class Rate(models.Model):
    user=models.ForeignKey(User,related_name="Rates",on_delete=models.CASCADE)
    music=models.ForeignKey(Music,related_name="Rates",on_delete=models.CASCADE)
    stars=models.ForeignKey(Star,related_name="Rates",on_delete=models.CASCADE)

