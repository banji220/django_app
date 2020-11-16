from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # the first Item of render() function should be request and the we define our templates, blog/home.htlm, blog is sub-dir !
    # request ----> HttpResponse (we should either use HttpResponse or exception!)
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")