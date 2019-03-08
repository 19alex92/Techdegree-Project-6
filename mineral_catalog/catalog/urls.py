from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.mineral_list),
    path('detail/', views.mineral_detail),
]