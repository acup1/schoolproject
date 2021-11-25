from django.http.response import HttpResponse
from django.shortcuts import render


def mainpage(request):
    return render(request,"main/main.html")

def pr(request):
    return render(request,"main/pr.html")
