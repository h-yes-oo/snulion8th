from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feed/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        photo =  request.FILES.get('photo', False)
        content = request.POST['content']
        Feed.objects.create(content=content, author= request.user, photo=photo)
        return redirect('/feeds') 

def new(request):
    return render(request, 'feed/new.html')

def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request,'feed/show.html',{'feed':feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author = request.user )
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')