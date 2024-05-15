"""
This file is used to configure the app name for the Django project.
"""

from django.apps import AppConfig

class MemoriesConfig(AppConfig):
    """The configuration for the memories app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memories'
