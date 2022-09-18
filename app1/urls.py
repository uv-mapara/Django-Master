from django.urls import path
from app1.views import login1,logout,register,update,delete,show

urlpatterns = [
    path('show/',show,name='show'),
    path('login1/',login1,name='login'),
    path('logout/',logout,name='logout1'),
    path('reg/',register,name='reg'),
    path('<int:id>/update/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
]
