"""
This module contains the views for the memories app.
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def make_memories(request):
    '''The view for the make_memories page.'''
    return render(request, 'memories/make_memories.html')
