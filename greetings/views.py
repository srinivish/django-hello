from django.shortcuts import render

# Create your views here.
# greetings/views.py

from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, world! This is your Django app running in Docker.")
