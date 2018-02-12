from django.urls import path

from . import views

urlpatterns = [
    path('hola/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
