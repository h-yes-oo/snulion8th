from django.shortcuts import render
from .models import Feed
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds':feeds})
    elif request.method == 'POST':
        photo = request.FILES.get('photo', False)
        content = request.POST['content']
        Feed.objects.create(author = request.user, content=content, photo=photo) 
        return redirect('/feeds')


def new(request):
    return render(request, 'feedpage/new.html')

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'feedpage/signup.html')