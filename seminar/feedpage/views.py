from django.shortcuts import render
from .models import Feed, FeedComment, Like
# 추가. (참고: .models == feedpage.models)
from django.shortcuts import redirect
from django.contrib.auth.models import User
# feedpage/view.py
...
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content, author=request.user)
        return redirect('/feeds')
    
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds':feeds})

def new(request):
    return render(request, 'feedpage/new.html')

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def show(request, id):
    feed=Feed.objects.get(id=id)
    if request.method == 'POST':
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        Feed.objects.filter(id=id).update(title=feed.title, content=feed.content)
    
    return render(request, 'feedpage/show.html', {'feed': feed})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

def feed_like(request, pk):
    feed = Feed.objects.get(id = pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    return redirect ('/feeds')