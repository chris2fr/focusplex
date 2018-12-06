from django.shortcuts import get_object_or_404, render
from .models import Who, WhatEtc

# Create your views here.

def index(renderer):
    return render(request, 'why/index.html', {})

def who(renderer, who_id):
    return render(request, 'why/who.html', {})

def what(renderer, whatetc_id):
    return render(request, 'why/whatetc.html', {})