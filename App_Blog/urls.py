from django.urls import path
from App_Blog import views

app_name= "App_Blog"

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/', views.blog_details, name='blog_details'),
    path('liked/', views.liked, name='liked_post'),
    path('unliked/', views.unliked, name='unliked_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),





]
