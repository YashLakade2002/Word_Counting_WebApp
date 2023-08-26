from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post', views.index, name='post-index'),
    path('counter', views.counter, name='counter'),
    path('post_detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post-delete'),
]
