"""Url routing"""

from django.urls import path
from therapists_profiles import views

urlpatterns = [
    path('profiles/', views.profiles),
    path('profiles/<int:id>/', views.profile)
]
