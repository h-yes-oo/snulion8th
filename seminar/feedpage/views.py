from django.shortcuts import render
from .models import Feed, FeedComment, Like
from django.shortcuts import redirect
from django.contrib.auth.models import User

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
        Feed.objects.create(title=title,content=content, author=request.user)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    if request.method == 'GET':
        feed=Feed.objects.get(id=id)
        return render(request, 'feedpage/show.html', {'feed':feed})
    elif request.method == 'POST':
        # Feed.objects.all()
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.filter(id=id).update(title=title, content=content, author = request.user)
        return redirect("/feeds/%d/" %id)

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed':feed})


def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content ,author = request.user)
    return redirect('/feeds')

def delete_comment(request, id, cid):
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
    return redirect ('/feeds')