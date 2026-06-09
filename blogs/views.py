from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category

# Create your views here.

def posts_by_categories(request, category_id):
  # Fetch the posts that belong to the category with the given category_id.
  posts = Blog.objects.filter(status='published', category_id=category_id)
  categories = Category.objects.all()
  # try:
  #   category = Category.objects.get(id=category_id)
  # except Category.DoesNotExist:
  #   category = None
  category = get_object_or_404(Category, id=category_id)

  context = {
    'posts': posts,
    'categories': categories,
    'category': category,
  }
  return render(request, 'posts_by_categories.html', context)

def blog_detail(request, blog_slug):
  single_blog = get_object_or_404(Blog, slug=blog_slug, status='published')
  context = {
    'single_blog': single_blog
  }
  return render(request, 'blog_detail.html', context)