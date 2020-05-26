from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Follow
from django.shortcuts import redirect

def signup(request):
    if request.method  == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        
        if password1 != password2:
            res_data = {}
            res_data['error'] = "비밀번호가 일치하지 않습니다" 
            return render(request, 'accounts/signup.html', res_data)
        else:
            user = User.objects.create_user(username=username,password=password1)
            auth.login(request, user)
            Profile.objects.filter(user = user).update(college = request.POST['college'],\
                            major = request.POST['major'], email = request.POST['email'],\
                            birthday = request.POST['birthday'], address = request.POST['address'])
            return redirect('/feeds')

    elif request.method == 'GET':
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
        else:
            return render(request, 'accounts/login.html')
            # , 'error':'username or password is incorrect')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logged_out.html')

def profile_edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        Profile.objects.filter(user = user).update(college = request.POST['college'], \
                major = request.POST['major'], email = request.POST['email'], \
                birthday = request.POST['birthday'], address = request.POST['address'])
        return redirect('/feeds')

    elif request.method == 'GET':
        return render(request, 'accounts/profile_edit.html')

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