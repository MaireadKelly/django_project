from django.shortcuts import render
fron django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")