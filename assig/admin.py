from django.contrib import admin

from assig.models import About, SocialLinks

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
  list_display = ('about_heading', 'created_at', 'updated_at')
  def has_add_permission(self, request):
    # Allow adding only if there are no existing About instances
    if About.objects.count() == 0:
      return True
    return False

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLinks)
