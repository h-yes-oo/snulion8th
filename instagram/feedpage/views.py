from django.shortcuts import render
from .models import Feed  # 추가. (참고: .models == feedpage.models)
from django.shortcuts import redirect

# Create your views here.


def index(request):
    if request.method == 'GET':  # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    elif request.method == 'POST':  # create(form을 이용하여 submit한 형태)
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')


def new(request):
    return render(request, 'feedpage/new.html')
