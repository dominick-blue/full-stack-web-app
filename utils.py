from django.db.models import Q
from .models import Blog, Tag


def searchBlogs(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)
    

    blogs = Blog.objects.distinct().filter(Q(description__icontains=search_query) | Q(tags__in=tags) |
    Q(title__icontains=search_query))

    return blogs, search_query 