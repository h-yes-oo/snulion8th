from django.shortcuts import render, redirect
from .models import Feed, Feedcomment


def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES.get('photo', False)
        Feed.objects.create(title=title, content=content, photo=photo)
        return redirect('/feeds') 


def new(request):
    return render(request, 'feedpage/new.html')

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    Feedcomment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = Feedcomment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')