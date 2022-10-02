from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models

 

def index(request):
    mymembers=Members.objects
    