from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('artwork/<int:pk>/', views.artwork_detail, name='artwork_detail'),
]