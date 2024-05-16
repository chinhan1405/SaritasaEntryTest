"""
This module contains the views for the memories app.
"""

import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponseRedirect
from memories.models import Place

def home(request: HttpRequest):
    '''The view for the index page.'''
    memories = Place.find_all()
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect('/login')
    return render(request, 'memories/home.html', {'memories': memories, 'username': user.username})

@csrf_exempt
def map_(request: HttpRequest):
    '''The view for the make_memories page.'''
    if request.method == 'POST':
        place = Place()
        place.account = request.user
        place.name = request.POST.get('name', '')
        place.memory = request.POST.get('memory', '')
        place.date = datetime.datetime.now()
        place.longitude = request.POST.get('longitude', 0)
        place.latitude = request.POST.get('latitude', 0)
        place.save()
        return HttpResponseRedirect('/')
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect('/login')
    memories = Place.find_by_account(user)
    return render(request, 'memories/map.html', {'memories': memories})

def login(request: HttpRequest):
    '''The view for the login page.'''
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'memories/login.html')
