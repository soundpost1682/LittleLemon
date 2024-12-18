from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [

    
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    

]