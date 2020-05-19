from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
  if request.method == 'GET':
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html',{'feeds':feeds})

  elif request.method =='POST':
    title = request.POST['title']
    content = request.POST['content']
    Feed.objects.create(title = title, content = content)
    return redirect('/feeds/')


def new(request):
  return render(request, 'feedpage/new.html')

def show(request, id):
  feed = Feed.objects.get(id = id)
  if request.method=='GET':
    return render(request, 'feedpage/show.html',{'feed':feed})

  elif request.method == 'POST':
    feed.title=request.POST['title']
    feed.content=request.POST['content']
    feed.save()

    redirect_to = request.GET.get('next')
    return redirect(redirect_to)

def delete(request, id):
  feed = Feed.objects.get(id = id)
  feed.delete()
  return redirect('/feeds/')

def update(request, id):
  feed = Feed.objects.get(id = id )
  redirect_to = request.GET.get('next')
  return render(request,'feedpage/update.html',{'feed':feed,'redirect_to':redirect_to})