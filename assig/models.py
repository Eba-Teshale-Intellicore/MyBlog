from django.db import models

# Create your models here.

class About(models.Model):
  about_heading = models.CharField(max_length=200)
  about_descriptions = models.TextField(max_length=2000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'About'

  def __str__(self):
    return self.about_heading


# class Social_Links:
class SocialLinks(models.Model):
  platform = models.CharField(max_length=100)
  link = models.URLField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.platform