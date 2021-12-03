from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index,name="home"),
    path('registration/', views.registration, name='reg'),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]
