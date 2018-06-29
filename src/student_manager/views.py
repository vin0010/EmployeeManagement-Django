from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def get_student(request):
    return HttpResponse("<h1>Welcome Student<h1>")
