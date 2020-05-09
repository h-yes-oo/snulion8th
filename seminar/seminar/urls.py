"""seminar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# seminar/urls.py
from django.contrib import admin
from django.urls import path
import feedpage.views      #추가
from django.conf.urls import include # 새로 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedpage.views.index, name='index'),   #추가
    path('feeds/', include('feedpage.urls')), # 항상 끝에도 쉼표를 붙여 줍시다
]