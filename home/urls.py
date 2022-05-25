from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthroizedView.as_view())
]