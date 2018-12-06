from django.shortcuts import get_object_or_404, render
from .models import Who, What

# Create your views here.

def index(renderer):
    return render(request, 'why/index.html', {})

def who(renderer, who_id):
    return render(request, 'why/who.html', {})

def what(renderer, what_id):
    return render(request, 'why/what.html', {})