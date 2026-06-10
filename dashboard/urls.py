from django.urls import path
from dashboard import views

urlpatterns = [
  path('', views.dashb , name='dashboard'),
  # Categories CRUD
  path('categories/', views.categories, name='categories'),
  path('categories/add/', views.add_categories, name='addCategories'),
  path('categories/edit/<int:pk>/', views.edit_categories, name='editCategories'),
  path('categories/delete/<int:pk>/', views.delete_categories, name='deleteCategories'),

  #Post CRUD
  path('blogs/', views.blogs, name="blogs"),
  
]