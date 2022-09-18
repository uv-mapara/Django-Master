from django.urls import path
from .views import signin,index,signup



urlpatterns = [
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),

    path('index/',index,name="index"),
]