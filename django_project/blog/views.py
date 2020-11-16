from django.shortcuts import render

posts = [
    {
        "author": "Banji", 
        "title" : "Blog Post 1", 
        "content" : "First Post Content", 
        "date_posted": "Jan 20th, 2020",
    },
    {
        "author": "James", 
        "title" : "Blog Post 2", 
        "content" : "Second Post Content", 
        "date_posted": "Aug 5th, 2020",
    }
]




def home(request):
    # the first Item of render() function should be request and the we define our templates, blog/home.htlm, blog is sub-dir !
    # request ----> HttpResponse (we should either use HttpResponse or exception!)
    context = {
        "posts" : posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")