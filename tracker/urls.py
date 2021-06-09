from tracker.views import country, index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index),
    path('country-wise',country),
]
