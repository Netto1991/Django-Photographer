# -*- coding: utf-8 -*-
from django.urls import path
from . import views
app_name = 'fotopage'
urlpatterns = [
        path('', views.index, name = 'index'),
        path('about/', views.about, name = 'about'),
        path('portfolio/', views.portfolio, name = 'portfolio'),
        path('price/', views.price, name = 'price'),
        path('specialoffer/', views.specialoffer, name = 'specialoffer'),
        path('<str:slug>/', views.AlbumDetail.as_view(), name='album'),
        ]