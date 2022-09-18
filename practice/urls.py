from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image/',include('image.urls')),
    path('math/',include('mathproblems.urls')),
    path('app1/',include('app1.urls')),
    path('Login/',include(('Login.urls','login'))),
    path('CBV/',include(('CBV.urls','CBV'))),
    path('FBV/',include('FBV.urls')),
    path('session/',include('session_use.urls')),
    path('auth/',include('django.contrib.auth.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
