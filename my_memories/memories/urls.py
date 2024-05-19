"""
This module is used to configure the URL patterns for the memories app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map_, name='map'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_handler, name='logout'),
]
