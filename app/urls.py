from django.conf.urls import url
from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('location/', views.LocationView.as_view(), name='location'),
     path('login/', views.LoginView.as_view(), name='login'),
]