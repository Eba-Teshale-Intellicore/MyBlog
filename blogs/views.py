from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category
from django.db.models import Q

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


def search(request):
  keyword = request.GET.get('keyword')
  if keyword:
    # search_results = Blog.objects.filter(title__icontains=keyword, status='published')
    search_results = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
  else:
    search_results = Blog.objects.none()

  context = {
    'search_results': search_results,
    'keyword': keyword,
  }
  print(search_results)

  return render(request, 'search.html', context)