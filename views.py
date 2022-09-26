from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Blog, Tag
from .forms import BlogForm
from .utils import searchBlogs
import django_filters


def blogs(request):
    blogs, search_query = searchBlogs(request)
    context = {'blogs':blogs, 'search_query':search_query}
    return render(request, 'blogs/blogs.html', context)


def blog(request, primary_key):
    blog_obj = Blog.objects.get(id=primary_key)
    return render(request, 'blogs/single-blog.html', {'blog':blog_obj})

@login_required(login_url="login")
def create_blog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    context = {'form': form}
    return render(request, "blogs/blog_form.html", context)

@login_required(login_url="login")
def update_blog(request, primary_key):
    blog = Blog.objects.get(id=primary_key)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    context = {'form': form}
    return render(request, "blogs/blog_form.html", context)

@login_required(login_url="login")
def delete_blog(request, primary_key):
    blog = Blog.objects.get(id=primary_key)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    context = {'object':blog}
    return render(request, 'blogs/delete_template.html', context)

