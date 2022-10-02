from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Members

def index(request):
    mymembers=Members.objects.all().values()
    output=''
    for x in mymembers:
        output+=['firstname']
    return http
    