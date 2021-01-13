from django.contrib import admin
from django.urls import path
from Pythonlearners import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('join',views.join,name="join"),
    path('peo',views.peo,name="Members"),
    path('about',views.about,name="about")
]
