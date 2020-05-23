from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile, Follow
# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['password1'] == request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            Profile.objects.filter(user=user).update(college=request.POST['college'], major=request.POST['major'])
            user.refresh_from_db()
            auth.login(request,user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
        else:
            return render(requset,'accounts/login.html')
    
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logged_out.html')

def changeinfo(request, id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        User.objects.filter(id=id).update(username=request.POST['username'])
        Profile.objects.filter(user=user).update(college=request.POST['college'], major=request.POST['major'])
        user.refresh_from_db()
        return redirect('/feeds')
    else:
        return render(request, 'accounts/changeinfo.html')

def follow_manager(request, pk):
    follow_from = Profile.objects.get(user_id = request.user.id)
    follow_to = Profile.objects.get(user_id = pk)

    try:
        following_already = Follow.objects.get(follow_from=follow_from, follow_to=follow_to)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        # Follow.objects.create(follow_from=follow_from, follow_to=follow_to)
        f = Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()

    return redirect('/feeds')