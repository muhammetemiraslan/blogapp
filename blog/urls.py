from django.urls import path
from . import views

# 127.0.0.1:8000/ => index
# 127.0.0.1:8000/index     => index
# 127.0.0.1:8000/blogs     => blogs
# 127.0.0.1:8000/blogs/3   => blog-details

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]