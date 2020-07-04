from django.shortcuts import render
from .models import Feed, FeedComment, Like, CommentLike
# 추가. (참고: .models == feedpage.models)
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

# feedpage/view.py
...
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo =  request.FILES.get('photo', False) #사진 field가 비어있어도 되도록! 
        Feed.objects.create(title=title, content=content, author= request.user, photo=photo)
        return redirect('/feeds')
    
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds':feeds})

def new(request):
    return render(request, 'feedpage/new.html')

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def show(request, id):
    feed=Feed.objects.get(id=id)
    if request.method == 'POST':
        feed.title = request.POST['title']
        feed.content = request.POST['content']
        Feed.objects.filter(id=id).update(title=feed.title, content=feed.content)
    
    return render(request, 'feedpage/show.html', {'feed': feed})

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content, author=request.user)
    new_comment = FeedComment.objects.latest('id')

    context = {
        'fid': id,
        'username': new_comment.author.username,
        'content': new_comment.content,
    }
    return JsonResponse(context)

def delete_comment(request, id, cid):
    c = FeedComment.objects.get(id=cid)
    c.delete()

    # context = {
    #     'fid': id,
    #     'cid': cid
    # }
    # return JsonResponse(context)
    return redirect('/feeds')

def feed_like(request, pk):
    feed = Feed.objects.get(id=pk)
    like_list = feed.like_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        feed.like_set.get(user_id = request.user.id).delete()
    else:
        if request.user.id:
            Like.objects.create(user_id = request.user.id, feed_id = feed.id)
        
    context = {
        'fid': feed.id,
        'like_count': like_list.count()
    }

    return JsonResponse(context)

def comment_like(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    like_list = comment.commentlike_set.filter(user_id = request.user.id)
    if like_list.count() > 0:
        comment.commentlike_set.get(user_id = request.user.id).delete()
    else:
        if request.user.id:
            CommentLike.objects.create(user_id = request.user.id, comment_id = comment.id)
    
    context = {
        'cid': cid,
        'fid': id,
        'like_count': like_list.count(),
    }
    return JsonResponse(context)

