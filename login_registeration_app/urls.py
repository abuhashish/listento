from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
        path('',views.root),
        path('login',views.login),
        path('home',views.home),
        path('register',views.register),
        path('logins',views.logins),
        path('artists', views.artists),
        path('userprofile', views.userprofile),
        path('artistprofile', views.artistprofile),
        path('songpage',views.songpage),
        path('adduser',views.adduser),
        path('logout',views.logout),
        path('addmusic', views.addmusic),
        path('delete/<int:id>',views.delete)
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)