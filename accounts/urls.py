from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),

]
