"""
This module is used to configure the URL patterns for the memories app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('makememories/', views.make_memories, name='makememories'),
]
