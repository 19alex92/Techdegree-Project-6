from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('minerals/', views.mineral_list),
    path('minerals/detail/', views.mineral_detail),
]