from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,"main.html")