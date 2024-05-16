"""
This file is used to test the models, views, and forms of the memories app.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from memories.models import Place

class PlaceTestCase(TestCase):
    '''Test the Place model.'''
    def setUp(self):
        '''Set up the test.'''
        self.user = User.objects.create_user('test_user', 'test_user', 'test@user')
        self.place = Place.objects.create(
            account=self.user,
            name='test_place',
            memory='test_memory',
            date='2021-01-01')

    def test_find_by_account(self):
        '''Test the find_by_account method.'''
        self.assertEqual(Place.find_by_account(self.user).count(), 1)

    def test_find_all(self):
        '''Test the find_all method.'''
        self.assertEqual(Place.find_all().count(), 1)
