from django.contrib import admin
from django.urls import path
import feedpage.views
import accounts.views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedpage.views.index, name='index'),
    path('feeds/', include('feedpage.urls')),
    # path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', accounts.views.signup, name='signup'),
]
 