from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Categories for blog posts model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

# Blog post model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=400, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to= 'uploads/%Y/%m/%d/')
    short_description = models.CharField(max_length=500)
    blog_body = models.CharField(max_length=20000)
    status = models.CharField(choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title