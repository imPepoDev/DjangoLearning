from django.urls import path
from . import views

urlpatterns = [
    # Blog Pages
    path('', views.my_view),
    path('casca/', views.receba),
]
