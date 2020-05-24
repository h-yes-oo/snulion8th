from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import Profile, Follow
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password1']
            )
            # profile=Profile.objects.create(user=user)
            user.profile.college=request.POST['college']
            user.profile.major=request.POST['major']
            user.profile.birth=request.POST['birth']
            user.profile.email=request.POST['email']

            user.profile.save()

            auth.login(request, user)
            return redirect('/feeds/')
    return render(request, 'accounts/signup.html')


def edit(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user

            user.username=request.POST['username']
            if request.POST['password1']==request.POST['password2']:
                password=request.POST['password1']
            else:
                return render(request, 'accounts/edit_pwfail.html')
            user.save()

            user.profile.college=request.POST['college']
            user.profile.major=request.POST['major']
            user.profile.birth=request.POST['birth']
            user.profile.email=request.POST['email']
            user.profile.save()
        return redirect('/feeds/')
    return render(request, 'accounts/edit.html')


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


# def login(request):
#     if request.method == 'POST':
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:             
#             auth.login(request, user) #로그인을 시켜줌
#             return redirect('/feeds/')
#     return render(request, 'accounts/login.html')

# def logout(request):
#     django_logout(request)
#     return redirect('/feeds/')
