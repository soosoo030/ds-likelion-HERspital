import requests
from django.shortcuts import render

def detail(request):
    return render(request, "community/detail.html")
def communityList(request):
    return render(request, "community/communityList.html")
def expertList(request):
    return render(request, "community/expertList.html")
def consulting(request):
    return render(request, "community/consulting.html")
def communityWrite(request):
    return render(request, "community/communityWrite.html")