from django.shortcuts import render
from django.shortcuts import redirect
from .models import Feed, FeedComment
from django.contrib.auth.models import User
from .models import Feed, FeedComment, Like, FeedCommentLike

# Create your views here.
...
def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title = title, content = content, author = request.user)
        return redirect('/feeds') 
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds':feeds})
def new(request):
    return render(request, 'feedpage/new.html')
def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request,'feedpage/show.html',{'feed':feed})
def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')
def edit(request,id):
    if request.method == 'GET':
        feed=Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed': feed})
    elif request.method == 'POST': 
        feed=Feed.objects.get(id=id)
        feed.title=request.POST['title']
        feed.content=request.POST['content']
        feed.save()
        feed.update_date()
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

def feedcomment_like(request, pk, cid):
    feedcomment = FeedComment.objects.get(id = cid)
    feedcommentlike_list = feedcomment.feedcommentlike_set.filter(user_id = request.user.id)
    if feedcommentlike_list.count() > 0:
        feedcomment.feedcommentlike_set.get(user_id = request.user.id).delete()
    else:
        FeedCommentLike.objects.create(user_id = request.user.id, feedcomment_id = feedcomment.id)
    return redirect ('/feeds')