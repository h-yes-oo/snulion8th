from django.shortcuts import render
from .models import Feed, FeedComment, Like, CommentLike  
from django.shortcuts import redirect
from django.contrib.auth.models import User 

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content, author = request.user)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html', {'feed':feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed':feed})

def update(request, id):
    feed = Feed.objects.get(id=id)
    feed.title = request.POST['title']
    feed.content = request.POST['content']
    feed.save()
    return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author = request.user)
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

def comment_like(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    like_list = c.commentlike_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        c.commentlike_set.get(user_id = request.user.id).delete()
    else:
        CommentLike.objects.create(user_id = request.user.id, feedcomment_id = c.id)
    return redirect ('/feeds')
