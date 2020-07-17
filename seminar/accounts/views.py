from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Follow
from django.shortcuts import redirect
from django.db.models.signals import post_save


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        password_check = request.POST["password2"]
        college = request.POST["college"]
        major = request.POST["major"]
        if password == password_check: 
            user = User.objects.create_user(username=username, email=email, password=password)
            user.profile.college = college
            user.profile.major = major
            user.save()

            login_user = django_authenticate(username=username, password=password)
            django_login(request, login_user)
            return JsonResponse({"response": "signup success"})

def login(request):
    if request.method == "POST":
        user = auth.authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/login.html')


def profile_update(request, id):
    # 마이페이지에서 보냈을 때 실행
    if request.method == "POST":
        user = User.objects.get(id=id)
        user.username = request.POST['username']
        user.major = request.POST['major']
        user.college = request.POST['college']
        user.sns = request.POST['sns']
        user.save()
        return redirect('/feeds/')
    # 베이스에서 눌렀을 때 링크 타고 가는 것 
    return render(request, 'accounts/mypage.html')


def follow_manager(request, pk):
    follow_from = Profile.objects.get(user_id = request.user.id)
    follow_to = Profile.objects.get(user_id = pk)

    try:
        following_already = Follow.objects.get(follow_from = follow_from, follow_to = follow_to)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        f = Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()

    return redirect('/feeds/')    