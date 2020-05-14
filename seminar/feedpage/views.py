from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        new_feed = Feed(title=title, content=content)
        new_feed.save()
        return redirect('/feeds')


def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html', {'feed':feed})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed':feed})
    #if request.method == 'POST':
    #    title = request.POST['title']
    #    content = request.POST['content']
    #    edit_feed = Feed(title=title, content=content)
    #   edit_feed.save()
    #return redirect('/feeds')
    #return redirect('/feeds')
    #return render(request, 'feedpage/edit.html', {'feed':feed})

def update(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'POST':
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.save()
    return redirect('/feeds')
'''
def update(request, id):
    feed = Feed.objects.get(id=id)
    #if request.method == 'GET':
    #    feeds = Feed.objects.all()
    #    return render(request, 'feedpage/index.html', {'feeds': feeds})
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        update_feed = Feed(title=title, content=content)
        update_feed.save()
        return redirect('/feeds') -->
'''


def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')


