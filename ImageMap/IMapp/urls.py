from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Intro, name="Intro"),
    path('map',views.MAP,name="map"),
    path('royapuram',views.royapuram,name="royapuram"),
    path('vyaserpadi',views.vyaserpadi,name='vyaserpadi'),
    path('tondiarpet',views.tondiarpet,name="tondiarpet"),
    path('perambur',views.perambur,name="perambur"),
    path('ayanavaram',views.ayanavaram,name="ayanavaram"),
    path('eggmore',views.eggmore,name='eggmore')
]
