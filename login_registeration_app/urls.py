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
        path('artistprofile/<int:id>', views.artistprofile),
        path('songpage/<int:id>',views.songpage),
        path('adduser',views.adduser),
        path('logout',views.logout),
        path('addmusic/<int:id>', views.addmusic),
        path('delete/<int:id>',views.delete),
        path('requesttobeartist',views.requesttobeartist),
        path('admin/',views.admin),
        path('adminProfile',views.adminprofile),
        path('adminhandle',views.adminhandle),
        path('artistrequest',views.artistrequest),
        path('acceptartist/<int:id>',views.acceptartist),
        path('declineartist/<int:id>',views.declineartist),
        path('adminallusers',views.allusers),
        path('allmusic',views.allmusic),
        path('deleteuser/<int:id>',views.deleteuser),
        path('deletemusic/<int:id>',views.deletemusic),
        path('update/<int:id>',views.update),
        path('follow/<int:id>',views.follow),
        path('unfollow/<int:id>',views.unfollow),
<<<<<<< HEAD
        path('search',views.search)
=======
        path('release/',views.release),
        path('top10',views.top10),
        path('rate/<int:id>', views.rate_image),
>>>>>>> 8d1f07d630fa4a0dbaa698dc5f9e3c3c35e2a0ff
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)