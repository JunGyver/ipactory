from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tag', include('tag.urls')),
    path('patent', include('patent.url')),
    path('user', include('user.url')),
]
