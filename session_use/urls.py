from django.urls import path
from .views import dashboard,index,logout


urlpatterns = [
    #session
    path('',index, name='index'),
    path('logout/',logout, name='logout1'),
    path('dashboard/',dashboard, name='dashboard'),
]