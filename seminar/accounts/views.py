from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method  == 'POST':
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        username = request.POST.get('username', None)
        res_data = {}
        if not (password1 and password2 and username) :
            res_data['error'] = "사용자 이름과 비밀번호를 입력해주세요"
        elif password1 != password2:
            res_data['error'] = "비밀번호가 일치하지 않습니다" 
        else:
            user = User.objects.create_user(username=username,password=password1)
            auth.login(request, user)
            Profile.objects.filter(user = user).update(college = request.POST['college'],\
                            major = request.POST['major'], email = request.POST['email'],\
                            birthday = request.POST['birthday'], address = request.POST['address'])
            return redirect('/feeds')

        return render(request, 'accounts/signup.html', res_data)

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

def user_edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        Profile.objects.filter(user = user).update(college = request.POST['college'], \
                major = request.POST['major'], email = request.POST['email'], \
                birthday = request.POST['birthday'], address = request.POST['address'])
        return redirect('/feeds')

    elif request.method == 'GET':
        return render(request, 'accounts/user_edit.html')


