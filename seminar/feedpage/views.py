from django.shortcuts import render
from .models import Feed,FeedComment,Like, CommentLike
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request,'feedpage/index.html',{'feeds':feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES.get('photo',False)
        Feed.objects.create(title=title, content=content, author= request.user, photo=photo)
        return JsonResponse({"message":"created"},status=201)

def new(request):
    return render(request, 'feedpage/new.html')
   
def show(request, id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html',{'feed':feed})

def delete(request, id):
    feed=Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    if request.method=='GET':
        feed=Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed':feed})
    elif request.method=='POST':
        feed=Feed.objects.get(id=id)
        if len(request.POST["title"])!=0:
            feed.title=request.POST["title"]
        if len(request.POST["content"])!=0:
            feed.content=request.POST["content"]
        feed.save()
        return redirect('/feeds')

def delete_comment(request,id,cid):
    c=FeedComment.objects.get(id=cid)
    c.delete()

    context= { 
        'cid': cid,
        'fid': id,
    }
    
    return JsonResponse(context)

def create_comment(request,id):
    content=request.POST['content']
    FeedComment.objects.create(feed_id=id,content=content,author=request.user)
    new_comment = FeedComment.objects.latest('id')

    context = {
        'id': new_comment.id,
        'username': new_comment.author.username,
        'content': new_comment.content,
    }

    return JsonResponse(context)

def feed_like(request,pk):
    feed = Feed.objects.get(id = pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    
    context = {
        'fid': feed.id,
        'like_count': like_list.count()
    }
    
    return JsonResponse(context)

def comment_like(request,id,cid):
    feedcomment=FeedComment.objects.get(id=cid)
    like_list=feedcomment.commentlike_set.filter(user_id=request.user.id)
    if like_list.count()>0:
        feedcomment.commentlike_set.get(user_id=request.user.id).delete()
    else:
        CommentLike.objects.create(user_id=request.user.id,comment_id=feedcomment.id)
    like_count=Count('like_users')

    context={
        'cid': cid,
        'fid': id,
        'like_count': like_list.count()
    }

    return JsonResponse(context)

def map(request):
    return render(request,'feedpage/map.html')