from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Follow
from django.shortcuts import redirect
from django.db.models.signals import post_save


def signup(request):
    if request.method == "POST":
        # username 없이 submit할 경우 오류 페이지가 뜨는 문제를 해결하기 위한 예외처리(?)
        if not request.POST['username']:
            return render(request, 'accounts/signup.html')
        # username 입력 되었을 때, 즉 정상적인 경우에 실행되는 코드
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1']
            )
            # 회원가입 시 자동으로 프로필 저장
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            user.profile.sns = request.POST['sns']
            user.profile.birth = request.POST['birth']

            user.save()
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html/')


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