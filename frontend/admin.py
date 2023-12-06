from django.contrib import admin
from .models import Website


#? Register your websites here to be visible in admin interface
@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'scraped_at', 'language')
