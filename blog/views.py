from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog.models import Blog

# Create your views here.

data = {
    "blogs": [
        {
            "id": 1,
            "title": "web geliştirme kursu",
            "image": "img1.png",
            "is_active": True,
            "is_home": False,
            "description": "iyi bir kurs"
        },
        {
            "id": 2,
            "title": "django geliştirme kursu",
            "image": "img2.png",
            "is_active": True,
            "is_home": True,
            "description": "çok iyi bir kurs"
        },
        {
            "id": 3,
            "title": "python geliştirme kursu",
            "image": "img1.png",
            "is_active": False,
            "is_home":  True,
            "description": "çok çok iyi bir kurs"
        }
    ]
}

def home(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True)
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })

