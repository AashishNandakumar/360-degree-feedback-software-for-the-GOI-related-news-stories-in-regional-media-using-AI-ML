from django.contrib import admin
from .models import Websites, ENewspapers, YouTubeVideos, ProcessedWebsites, ProcessedENewspapers, ProcessedYouTubeVideos, PIBOfficials, NotificationsLog

# Register your models here

# Source Schema Models
@admin.register(Websites)
class WebsitesAdmin(admin.ModelAdmin):
    list_display = ('website_id', 'url', 'scraped_at', 'language')

@admin.register(ENewspapers)
class ENewspapersAdmin(admin.ModelAdmin):
    list_display = ('e_newspaper_id', 'image_path', 'scanned_at', 'edition')

@admin.register(YouTubeVideos)
class YouTubeVideosAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_url', 'downloaded_at')

#! Processed_and_analyzed Schema Models
@admin.register(ProcessedWebsites)
class ProcessedWebsitesAdmin(admin.ModelAdmin):
    list_display = ('processed_website_id', 'sentiment', 'processed_at', 'source_website')

@admin.register(ProcessedENewspapers)
class ProcessedENewspapersAdmin(admin.ModelAdmin):
    list_display = ('processed_e_newspaper_id', 'sentiment', 'processed_at', 'source_e_newspaper')

@admin.register(ProcessedYouTubeVideos)
class ProcessedYouTubeVideosAdmin(admin.ModelAdmin):
    list_display = ('processed_video_id', 'sentiment', 'processed_at', 'source_video')

# Notification Schema Models
@admin.register(PIBOfficials)
class PIBOfficialsAdmin(admin.ModelAdmin):
    list_display = ('official_id', 'name', 'department')

@admin.register(NotificationsLog)
class NotificationsLogAdmin(admin.ModelAdmin):
    list_display = ('notification_id', 'official_id', 'sentiment', 'sent_at')

