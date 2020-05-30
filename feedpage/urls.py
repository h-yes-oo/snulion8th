from django.urls import path
from feedpage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/',views.edit, name="edit"),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/like/', views.feed_like, name='like'),
    path('<int:pk>/like_comment/', views.comment_like, name='comment_like'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)