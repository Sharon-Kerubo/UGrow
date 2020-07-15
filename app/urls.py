from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
     path('', views.index, name='index'),
     path('explore/kisii/', views.kisii, name='kisii'),
     path('explore/kisumu/', views.kisumu, name='kisumu'),
     path('explore/eldoret/', views.eldoret, name='eldoret'),
     path('explore/meru/', views.meru, name='meru'),
     path('explore/kiambu/', views.kiambu, name='kiambu'),
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('county_data/', views.county_datasets, name='county'),
     path('soils_data/', views.soils_datasets, name='soils'),
     path('soilph_data/', views.soilph_datasets, name='soilph'),
     path('crop_data/', views.crop_datasets, name='crop'),
]