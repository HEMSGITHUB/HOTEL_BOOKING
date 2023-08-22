from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('booking/',views.booking,name='index'),
    path('',views.home,name='booking'),
    path('index', views.index, name='index'),
    path('booking/userDetailsAdd',views.userDetailsAdd,name='index'),
    path('edituser/<int:id>', views.edituser, name='edituser'),
    path('userDetailsUpdate/<int:id>', views.userDetailsUpdate, name='userDetailsUpdate'),
    path('deleteuser/<int:id>', views.userDetailsDelete, name='deleteuser'),
]
