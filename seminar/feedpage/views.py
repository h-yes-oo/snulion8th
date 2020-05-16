# seminar/feedpage/views.py
from django.shortcuts import render
from .models import Feed  
from django.shortcuts import redirect

# index 함수 코드 변경
def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds') 

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
    feed = Feed.objects.get(id = id)
    return render(request, 'feedpage/edit.html', {'feed':feed })


def update(request, id):
    feed = Feed.objects.get(id = id)
    feed.title =request.POST.get('title')
    feed.content =request.POST.get('content')
    feed.save()
    return redirect('/feeds')

