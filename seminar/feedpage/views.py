from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

# Create your views here.
def index(request): # 원래 있던 index 함수 수정
    if request.method == 'GET':
        feeds = Feed.objects.all()
        # Feed object를 불러와서 feeds에 다 저장
        return render(request, 'feedpage/index.html', {'feeds': feeds})
        # 이 feeds를 feedpage에 넘겨주겠다
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title,content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    if request.method == 'GET':
        feed=Feed.objects.get(id=id)
        return render(request, 'feedpage/show.html', {'feed':feed})
    elif request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        feed.save()
        return render(request, 'feedpage/show.html', {'feed':feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed':feed})