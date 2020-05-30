from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect


def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})
    elif request.method == 'POST': # create(form을 이용하여 submit한 형태) 
        content = request.POST['content']
        Feed.objects.create(content=content)
        return redirect('/feeds') 
def new(request):
    return render(request, 'feedpage/new.html')
def show(request,id):
    feed=Feed.objects.get(id=id)
    return render(request,'feedpage/show.html',{'feed':feed})
# Create your views here.
