from django.shortcuts import render
from .models import Feed, FeedComment, Like, LikeComment# 추가. (참고: .models == feedpage.models)
from django.shortcuts import redirect
from django.contrib.auth.models import User


def index(request): # 원래 있던 index 함수 수정.
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES.get('photo', False)
        Feed.objects.create(title=title, content=content, author = request.user, photo=photo)
        return redirect('/feeds') 

    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds':feeds})

def new(request):
    return render(request, 'feedpage/new.html')

def show(request,id):
    if request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.update(title=request.POST['title'], content=request.POST['content'])
        # Feed.objects.filter(id=id).update(title=request.POST['title'], content=request.POST['content'])
        return redirect('/feeds')

    elif request.method == 'GET':
        feed=Feed.objects.get(id=id)
        return render(request,'feedpage/show.html',{'feed':feed})

    # if  request.method == 'GET':
    #     feed=Feed.objects.get(id=id)
    #     return render(request,'feedpage/show.html',{'feed':feed})

    # elif request.method == 'POST' :
    #     feed = Feed.objects.get(id=id)
    #     feed.title = request.POST['title']
    #     feed.content = request.POST['content']
    #     feed.save()
    #     return redirect('/feeds')
    

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def edit(request, id):
    feed=Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html',{'feed':feed})

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    c=FeedComment.objects.get(id=cid)
    c.delete()
    return redirect ('/feeds')

def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() >0 :
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        Like.objects.create(user_id = request.user.id, feed_id = feed.id)
    return redirect ('/feeds')


def comment_like(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    like_list = comment.likecomment_set.filter(user_id=request.user.id)
    if like_list.count() >0 :
        comment.likecomment_set.get(user_id=request.user.id).delete()
    else :
        LikeComment.objects.create(user_id=request.user.id, comment_id=cid)
    return redirect ('/feeds')

