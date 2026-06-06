from django.shortcuts import render

from blogs.models import Blog

# Create your views here.

def posts_by_categories(request, category_id):
  # Fetch the posts that belong to the category with the given category_id.
  posts = Blog.objects.filter(status='published', category_id=category_id)

  context = {
    'posts': posts,
  }
  return render(request, 'posts_by_categories.html', context)

