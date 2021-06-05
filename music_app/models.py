from django.db import DefaultConnectionProxy, models
from django.db.models.fields import DateField
from login_registeration_app.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Music(models.Model):
    song_name=models.CharField(max_length=45)
    writer=models.CharField(max_length=45)
    composer = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lyrics=models.TextField()
    music = models.FileField(upload_to='audio/', blank=True)
    uploaded_by=models.ForeignKey(User,related_name="songs",on_delete=models.CASCADE)
    
RateChoices=[
    (0,'0-trash'),
    (1,'1-bad'),
    (2,'2-not bad'),
    (3,'3-good'),
    (4,'4-very good'),
    (5,'5-Amazing')
]
class Rate(models.Model):
    score=models.IntegerField(default=0)
    user=models.ForeignKey(User,related_name="Rates",on_delete=models.CASCADE)
    music=models.ForeignKey(Music,related_name="Rates",on_delete=models.CASCADE)
    validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ]
    

