from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author
from django.db.models.manager import Manager
# Create your views here.
def index(request):
    return HttpResponse('index')