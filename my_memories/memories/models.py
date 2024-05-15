"""
The models for places' memories.
"""

from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    '''A memory of a place.'''
    account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    name = models.CharField(max_length=255)
    memory = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.name)
