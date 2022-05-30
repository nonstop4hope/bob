from django.urls import path
from search.google import views

urlpatterns = [
    path('google', views.result)
]