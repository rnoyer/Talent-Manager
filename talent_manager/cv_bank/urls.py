from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.cv_bank_home,name='cv_bank_homepage'),
    path('add-profile', views.add_profile,name='cv_bank_add_profile'),
]
