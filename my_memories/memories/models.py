"""
The models for places' memories.
"""

import datetime
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

    objects = models.Manager()

    def __str__(self):
        return str(self.name)

    @staticmethod
    def find_by_account(account):
        '''Find all places by account.'''
        return Place.objects.filter(account=account)

    @staticmethod
    def find_all():
        '''Find all places.'''
        return Place.objects.all()

    @staticmethod
    def create_memory(account, longitude: float, latitude: float, name: str, memory:str):
        '''Create a memory.'''
        place = Place()
        place.account = account
        place.longitude = longitude
        place.latitude = latitude
        place.name = name
        place.memory = memory
        place.date = datetime.datetime.now()
        place.save()
