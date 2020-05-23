from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect

# Create your views here.
# feedpage/view.py
...
def index(request):
    if request.method =='GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html',{'feeds':feeds})
    elif request.method == 'POST':
        title= request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds/')
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds': feeds})

def new(request):
    return render(request, 'feedpage/new.html')

def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request,'feedpage/show.html',{'feed':feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    if request.method =='GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html',{'feed':feed})
    elif request.method=="POST":
        feed = Feed.objects.get(id=id)
        feed.title= request.POST['title']
        feed.content = request.POST['content']
        feed.save()
        return redirect('/feeds/')

def create_comment(request, id):
    content=request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c= FeedComment.objects.get(id=cid)
    c.delete()
    return redirect('/feeds')