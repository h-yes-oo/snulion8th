from django.shortcuts import render, redirect
from .models import Feed, FeedComment, Like, LikeComment
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content, author=request.user)
        return redirect('/feeds/')

    elif request.method == "GET":
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})


def new(request):
    return render(request, 'feedpage/new.html')


def show(request, id):
    feed = Feed.objects.get(id=id)

    if request.method == "POST":
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.save()
        return redirect('/feeds/')

    return render(request, 'feedpage/show.html', {'feed': feed})


def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds/')


def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})


def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(
        feed_id=id, content=content, author=request.user)
    return redirect('/feeds')


def delete_comment(request, id, commentid):
    comment = FeedComment.objects.get(id=commentid)
    comment.delete()
    return redirect('/feeds')


def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    like_list = feed.like_set.filter(user_id=request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id=request.user.id).delete()
    else:
        Like.objects.create(user_id=request.user.id, feed_id=feed.id)
    return redirect('/feeds')


def feedcomment_like(request, pk, commentid):
    feedcomment = FeedComment.objects.get(id=commentid)
    like_list = feedcomment.likecomment_set.filter(user_id=request.user.id)
    if like_list.count() > 0:
        feedcomment.likecomment_set.get(user_id=request.user.id).delete()
    else:
        LikeComment.objects.create(
            user_id=request.user.id, feedcomment_id=feedcomment.id)
    return redirect('/feeds')
