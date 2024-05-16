"""
This file is used to register the PlaceMemory model with the Django admin site.
This allows us to view and edit the PlaceMemory model from the Django admin site.
"""

from django.contrib import admin
from .models import Place

class PlaceMemoryAdmin(admin.ModelAdmin):
    '''The admin class for the PlaceMemory model.'''
    list_display = ('account', 'name', 'latitude', 'longitude')
    search_fields = ('name', 'account__username')

admin.site.register(Place, PlaceMemoryAdmin)
