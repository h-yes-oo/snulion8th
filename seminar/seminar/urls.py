from django.contrib import admin
from django.urls import path
import feedpage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feedpage.views.index, name='index'),   
]
