from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('courses/destroy/<id>', views.destroy_form),
    path('destroy/<id>', views.destroy)
]