from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('location/', views.LocationView.as_view(), name='location'),
     path('explore/kisii/', views.KisiiView.as_view(), name='kisii'),
     path('explore/kisumu/', views.KisiiView.as_view(), name='kisumu'),
     path('explore/eldoret/', views.KisiiView.as_view(), name='eldoret'),
     path('explore/meru/', views.KisiiView.as_view(), name='meru'),
     path('explore/kiambu/', views.KisiiView.as_view(), name='kiambu'),

]