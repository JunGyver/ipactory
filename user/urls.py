from django.urls import path
from .views import Login

urlpatterns = [
    path('login/', LogIn.as_view()),
]
