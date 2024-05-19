"""
This file is used to test the models, views, and forms of the memories app.
"""

import random
from django.test import TestCase
from django.contrib.auth.models import User
from memories.models import Place

class PlaceTestCase(TestCase):
    '''Test the Place model.'''
    def setUp(self):
        '''Set up the test.'''
        self.number_of_users = 5
        self.users = [User.objects.create_user(
                        'test' + str(i) + 'user',
                        'test_user',
                        'test' + str(i) + '@example.com')
                    for i in range(self.number_of_users)]

        for i, user in enumerate(self.users):
            Place.create_memory(
                account=user,
                longitude=random.uniform(-180, 180),
                latitude=random.uniform(-90, 90),
                name=(str(i)+'Test Place'),
                memory=(str(i)+'Test Memory'),
            )

    def test_model_find_by_account(self):
        '''Test the find_by_account method.'''
        self.assertEqual(Place.find_by_account(self.users[0]).count(), 1)

    def test_model_find_all(self):
        '''Test the find_all method.'''
        self.assertEqual(Place.find_all().count(), self.number_of_users)

    def test_create_memories(self):
        '''Test the create_memories method.'''
        Place.create_memory(self.users[0], 0, 0, 'Test Place', 'Test Memory')
        self.assertEqual(Place.find_by_account(self.users[0]).count(), 2)

    def test_fetch_memories(self):
        '''Test the fetch_memories method.'''
        for i, user in enumerate(self.users):
            Place.create_memory(
                account=user,
                longitude=random.uniform(-180, 180),
                latitude=random.uniform(-90, 90),
                name=(str(i)+'Test Place 2'),
                memory=(str(i)+'Test Memory 2'),
            )
        memories_num = 0
        for user in self.users:
            memories_num += Place.find_by_account(user).count()
        self.assertEqual(memories_num, 2 * self.number_of_users)
