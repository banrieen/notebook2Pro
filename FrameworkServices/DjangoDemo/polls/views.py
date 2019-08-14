from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, How  may I help you ?")
# Create your views here.
