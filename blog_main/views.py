from django.shortcuts import redirect, render
from blogs.models  import Category, Blog
from assig.models import About, SocialLinks
from .forms import SignupForm, LoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

def register(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      print(form.errors)
  else:
    form = SignupForm()

  context = {
    'form': form,
  }
  return render(request, 'signup.html', context)

def login(request):
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      user = auth.authenticate (username=username, password= password)
      if user is not None:
        auth.login(request, user)
        return redirect('home')
  else:
    form = LoginForm()
  
  context = {
    'form': form,
  }

  return render(request, 'login.html', context)


def logout(request):
  auth.logout(request)
  return redirect('home')