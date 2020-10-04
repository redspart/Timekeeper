from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("You are on the time_entry app")

def create_entry(request):
    pass

def update_entry(request):
    pass

def delete_entry(request):
    pass
