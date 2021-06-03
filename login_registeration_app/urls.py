from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
        path('',views.root),
        path('login',views.login),
        path('register',views.register),
        path('home',views.home),
        path('artists', views.artists),
        path('userprofile', views.userprofile),
        path('artistprofile', views.artistprofile),
        path('songpage',views.songpage)

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)