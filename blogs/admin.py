from django.contrib import admin
from blogs.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
  list_filter = ('status', 'is_featured', 'created_at')
  search_fields = ('title', 'author__username', 'category__category_name', 'status')
  list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)