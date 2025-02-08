from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.user_stats,name='user_stat'),
    path('events',views.events,name='events')
]
