from django.urls import path
from . import views


urlpatterns = [
    path("login", views.loginRes),
    path("signup", views.signupRes)
]