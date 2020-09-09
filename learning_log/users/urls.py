"""Defines URL patterns for users."""
#from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.conf.urls import url

urlpatterns = [
   #Login
   url(r'^login/$',views.login,name='login'),

   #Logout
   path('logout/',views.logout,name='logout'),

   #Register
   path('register/',views.register,name='register'),
   ]
