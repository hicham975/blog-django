from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display_article/<slug:slug>/', views.detail,name='detail'),
    path('all_article/<slug:slug>/', views.AllPostCategory,name='allposts'),
]
