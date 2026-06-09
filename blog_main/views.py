from django.shortcuts import render
from blogs.models  import Category, Blog
from assig.models import About, SocialLinks

def home(request):
  categories = Category.objects.all()
  blogs = Blog.objects.all()
  featured_posts = Blog.objects.filter(is_featured=True, status='published')
  posts = Blog.objects.filter(is_featured=False, status='published')
  about = About.objects.all()
  social_links = SocialLinks.objects.all()

  context = {
    'categories': categories,
    'blogs': blogs,
    'featured_posts': featured_posts,
    'posts': posts,
    'about': about,
    'social_links': social_links,
  }
  return render(request, 'home.html', context)