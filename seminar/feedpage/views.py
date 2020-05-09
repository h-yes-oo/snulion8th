from django.shortcuts import render
from .models import Feed 

def index(request):
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds': feeds})


