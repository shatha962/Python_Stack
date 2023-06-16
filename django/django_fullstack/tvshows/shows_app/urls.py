from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('shows/', views.all_shows),
    path('shows/new/', views.add_page),
    path('process', views.create),
    path('show/<id>', views.show)
]