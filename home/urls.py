from django.urls import path
from . import views

urlpatterns = [
    # Home Pages
    path('', views.home),
]
