from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse("Hello world")
# Create your views here.
def view2(request):
    return HttpResponse("Hello from extension site")
