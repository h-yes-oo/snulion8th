from django.shortcuts import render

# Create your views here.

# feedpage/view.py
def index(request):
    return render(request, 'feedpage/index.html')