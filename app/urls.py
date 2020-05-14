from django.urls import path
from .import views, models

app_name = 'app'

urlpatterns = [
     path('', views.index),
     path('explore/kisii/', views.kisii),
     path('explore/kisumu/', views.kisumu),
     path('explore/eldoret/', views.eldoret),
     path('explore/meru/', views.meru),
     path('explore/kiambu/', views.kiambu),
     path('signup/', views.signup),
     path('login/', views.login),
]