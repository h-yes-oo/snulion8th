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
from django.conf.urls import include
import feedpage.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',feedpage.views.index, name='index'),
    path('feeds/',include('feedpage.urls')),
    path('accounts/signup/', accounts.views.signup, name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('accounts/mypage/', accounts.views.mypage, name='mypage'),
    path('accounts/<int:pk>/follow/', accounts.views.follow_manager, name='follow'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)