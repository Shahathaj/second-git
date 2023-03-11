from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>this is my first project</h1></marquee>')