from django.urls import path
from .views import signup
from .views import Login

urlpatterns = [
    path("signup/",signup),
    path("login/",Login)
]

