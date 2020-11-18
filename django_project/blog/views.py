from django.shortcuts import render
from .models import Post




def home(request):
    # the first Item of render() function should be request and the we define our templates, blog/home.htlm, blog is sub-dir !
    # request ----> HttpResponse (we should either use HttpResponse or exception!)
    context = {
        "posts" : Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})