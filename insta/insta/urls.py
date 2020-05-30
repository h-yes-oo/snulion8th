from django.contrib import admin
from django.urls import path
import feedpage.views
from django.conf.urls import include # 새로 추가
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedpage.views.index, name='index'),
    path('feeds/', include('feedpage.urls')), # 항상 끝에도 쉼표를 붙여 줍시다
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)