from django.shortcuts import render
from blogs.models  import Category

def home(request):
  categories = Category.objects.all()
  return render(request, 'home.html', {'categories': categories})