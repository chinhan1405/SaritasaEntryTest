"""
This module contains the views for the memories app.
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import logout
from memories.models import Place

def home(request: HttpRequest):
    '''The view for the index page.'''
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect('/login')
    memories = Place.find_by_account(request.user)
    return render(request, 'memories/home.html', {'memories': memories, 'username': user.username})

@csrf_exempt
def map_(request: HttpRequest):
    '''The view for the make_memories page.'''
    if request.method == 'POST':
        account = request.user
        name = request.POST.get('name', '')
        memory = request.POST.get('memory', '')
        longitude = request.POST.get('longitude', 0)
        latitude = request.POST.get('latitude', 0)
        Place.create_memory(account, longitude, latitude, name, memory)
        return HttpResponseRedirect('/')
    user = request.user
    if user.is_anonymous:
        return HttpResponseRedirect('/login')
    memories = Place.find_by_account(user)
    return render(request, 'memories/map.html', {'memories': memories})

def login_view(request: HttpRequest):
    '''The view for the login page.'''
    print(request.method)
    return render(request, 'memories/login.html')

def logout_handler(request: HttpRequest):
    '''Handle the logout request.'''
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/login')
