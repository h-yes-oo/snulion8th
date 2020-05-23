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
from django.contrib import admin
from django.urls import path
import feedpage.views 
import accounts.views 
from django.conf.urls import include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedpage.views.index, name='index'),
    # include 덕분에 feeds/가 앞에 붙어서 작동한다. 
    path('feeds/', include('feedpage.urls')), 
    # django에 제공되는 것을 연결하기 때문에 account 아래 url 설정 안먹음ㅠ
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/profile_edit/<int:id>/', accounts.views.profile_edit, name='profile_edit'), 
    path('accounts/<int:pk>/follow/', accounts.views.follow_manager, name='follow'),
    # 항상 끝에도 쉼표를 붙여 줍시다 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
