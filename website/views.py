from django.shortcuts import render

# Create your views here.


def index(response):
    return render(response, "website/index.html")


def watch(request):
    return render(request, 'website/movie-detail.html')
