from django.urls import path
from feedpage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit',views.edit, name="edit"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)