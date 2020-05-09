from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.

def index(request):
  if request.method == 'GET':
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html',{'feeds':feeds})
  elif request.method =='POST':
    title = request.POST['title']
    content = request.POST['content']
    Feed.objects.create(title = title, content = content)
    return redirect('/feeds')

def jackyoung(request):
  return render(request, 'feedpage/jackyoung.html')

def new(request):
  return render(request, 'feedpage/new.html')

def show(request, id):
  feed = Feed.objects.get(id = id)
  if request.method=='GET':
    return render(request, 'feedpage/show.html',{'feed':feed})
  elif request.method == 'POST':
    feed.update_title(request.POST['title'])
    feed.update_content(request.POST['content'])
    return render(request, 'feedpage/show.html',{'feed':feed})

  feed = Feed.objects.get(id = id)
  return render(request, 'feedpage/show.html',{'feed':feed})

def delete(request, id):
  feed = Feed.objects.get(id = id)
  feed.delete()
  return redirect('/feeds')

def update(request, id):
  feed = Feed.objects.get(id = id )
  return render(request, 'feedpage/update.html',{'feed':feed})
  