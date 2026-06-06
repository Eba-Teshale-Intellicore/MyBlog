from django.shortcuts import render
from blogs.models  import Category, Blog

def home(request):
  categories = Category.objects.all()
  blogs = Blog.objects.all()
  featured_posts = Blog.objects.filter(is_featured=True, status='published')
  posts = Blog.objects.filter(is_featured=False, status='published')

  context = {
    'categories': categories,
    'blogs': blogs,
    'featured_posts': featured_posts,
    'posts': posts,
  }
  return render(request, 'home.html', context)