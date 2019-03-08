from django.urls import path, include

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index),
    path('minerals/', views.mineral_list),
    path('minerals/detail/<pk>', views.mineral_detail, name='detail'),
]