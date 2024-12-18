from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('', views.index, name='index'),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),

]