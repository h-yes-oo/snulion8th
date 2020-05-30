from django.shortcuts import render
from .models import Feed, FeedComment
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.

def main(request): 
    if request.method=='GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/main.html', {'feeds': feeds})
    elif request.method=='POST':
        content= request.POST['content']
        photo =  request.FILES.get('photo', False)
        Feed.objects.create(content=content, photo=photo)
        return redirect ('/feeds')

    feeds=Feed.objects.all()
    return render(request,'feedpage/main.html',{'feeds':feeds})

def create(request):
    return render(request, 'feedpage/create.html')

def read(request,id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/read.html',{'feed':feed})

def edit(request,id):
    if request.method=='GET':
        feed=Feed.objects.get(id=id)
        return render(request, 'feedpage/edit.html', {'feed':feed})
    elif request.method=='POST':
        feed=Feed.objects.get(id=id)
        if request.POST["content"]:
            feed.content=request.POST["content"]
        if request.POST['photo']:
            feed.photo=request.POST
        feed.save()
        feed.update_date()
        return redirect('/feeds')

def delete(request, id):
    feed=Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request,id):
    content=request.POST['content']
    FeedComment.objects.create(feed_id=id,content=content,author=request.user)
    return redirect('/feeds')