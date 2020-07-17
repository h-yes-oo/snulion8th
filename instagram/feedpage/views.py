from django.shortcuts import render
from django.shortcuts import redirect
from .models import Feed, FeedComment, Like
from django.contrib.auth.models import User

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        author = request.user.username
        content = request.POST['content']
        photo = request.FILES.get('photo', False)
        Feed.objects.create(content=content, photo=photo, author=request.user)
        return redirect('/feeds/')
    

def new(request):
    return render(request, 'feedpage/new.html')


def show(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html', {'feed': feed})


def delete(reqeust, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds/')


def update(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed':feed})
    elif request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.content = request.POST['content']
        feed.photo = request.FILES['photo_edit']
        feed.save()
    return redirect('/feeds/')


def feed_comment(request, id):
    FeedComment.objects.create(feed_id=id, author=request.user, content=request.POST['content'])
    return redirect('/feeds/')


def comment_delete(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    comment.delete()
    return redirect('/feeds/')


def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.filter(user_id = request.user).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    return redirect('/feeds/')
