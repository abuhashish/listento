from django.contrib import admin
from login_registeration_app.models import User
from music_app.models import Music

admin.site.register(User)
admin.site.register(Music)

# Register your models here.
