from django.shortcuts import render
from .models import Feed, FeedComment, Like, CommentLike
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds':feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # feed = Feed.objects.create(title=title, content=content, author=request.user)
        photo =  request.FILES.get('photo', False)
        Feed.objects.create(title=title, content=content, author= request.user, photo=photo)
        #return redirect('/feeds/%d/' %feed.id)#이건 get방식으로 url을 가서 다시 index로 돌아옴
        return redirect('/feeds')


def new(request):
    return render(request, 'feedpage/new.html')


def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html',{'feed':feed})#{'feed':feed}가 무슨의미?


def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')


def edit(request, id):
    if request.method == 'POST':
        feed=Feed.objects.get(id=id)
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.update_date()
        feed.save()
        return redirect('/feeds')


    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html',{'feed':feed})


def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content )
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
    
    return redirect('/feeds')


def comment_like(request, pk):
    feedcomment = FeedComment.objects.get(id = pk)
    like_list = feedcomment.commentlike_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feedcomment.commentlike_set.get(user_id = request.user.id).delete()
    else:
        CommentLike.objects.create(user_id = request.user.id, feedcomment_id = feedcomment.id)
    feed = Feed.objects.get(id = fid)
    qs = feed.feedcomment_set.all()
    unsorted_results = qs.all()
    sorted_results = sorted(unsorted_results, key= lambda t: t.thing_date())

    return redirect('/feeds')
