from django.shortcuts import render
from .models import Feed, FeedComment , Like
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request,'feedpage/index.html',{'feeds':feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES.get('photo',False)
        Feed.objects.create(title=title, content=content, author= request.user, photo=photo)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')

def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request,'feedpage/show.html',{'feed':feed})

def edit(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed': feed})
    elif request.method == 'POST':
        feed=Feed.objects.get(id=id)
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.save()
        feed.update_date()
        return redirect('/feeds/'+str(id)) 

def delete(request,id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request,id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    new_comment = FeedComment.objects.latest('id')

    context = {
        'comment': {
            'id': new_comment.id,
            'username': new_comment.author.username,
            'content': new_comment.content
        }
    }
    return JsonResponse(context)

def delete_comment(request,id,cid):
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
    context = {
        'fid': feed.id,
        'like_count': like_list.count()
    }
    
    return JsonResponse(context)

def map(request):
    return render(request,'feedpage/map.html')