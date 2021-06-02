from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
        path('',views.root),
        path('login',views.login),
        path('register',views.register),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)