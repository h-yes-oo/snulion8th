from django.shortcuts import render
from .models import Feed, FeedComment, Like, CommentLike
from django.shortcuts import redirect 
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        content = request.POST['content']
        photo =  request.FILES.get('photo', False) 
        Feed.objects.create(content=content, author= request.user, photo=photo)
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
        feed.content = request.POST['content']
        if request.FILES.get('photo') is None:
            feed.photo = feed.photo
        else:
            feed.photo = request.FILES.get('photo', False)

        feed.save()
        # Feed.objects.filter(id=id).update(content=feed.content, photo=feed.photo)
        # -> save로 하면 저장이되고, filter로 update하면 반영이 안되는 이유는...????ㅠ
        
    return render(request, 'feedpage/show.html', {'feed': feed})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed':feed})

def create_comment(request, id):
    content = request.POST.get('content')
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')

def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        if request.user.id:
            Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    return redirect ('/feeds')

def comment_like(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    like_list = comment.commentlike_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        comment.commentlike_set.get(user_id = request.user.id).delete()
    else:
        if request.user.id:
            CommentLike.objects.create(user_id = request.user.id, comment_id = comment.id)
    return redirect ('/feeds')
