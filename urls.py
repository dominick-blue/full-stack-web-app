from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('blog/<str:primary_key>/', views.blog, name="blog"),
    path('create-blog/', views.create_blog, name="create-blog"),
    path('update-blog/<str:primary_key>/', views.update_blog, name="update-blog"),
    path('delete-blog/<str:primary_key>/', views.delete_blog, name="delete-blog"),
]