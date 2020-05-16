from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds':feeds})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds/%d/' %feed.id)#이건 get방식으로 url을 가서 다시 index로 돌아옴

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