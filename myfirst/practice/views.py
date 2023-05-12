from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>hello world</h>")
def start(request):
    return HttpResponse("i welcome you to this test")    

def site(request) :
    return render(request,'site.html')   