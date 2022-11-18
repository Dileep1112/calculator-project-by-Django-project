from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    res=render(request, "home.html")
    return res

def calculate(request):
    n1=int(request.GET["t1"])
    n2=int(request.GET["t2"])
    b=request.GET["b"]
    if b=="add":
        res=n1+n2
    elif b=="sub":
        res=n1-n2
    elif b=="mul":
        res=n1*n2
    elif b=="div":
        res=n1/n2
    res=render(request,"result.html",context={"res":res})
    return res

