from django.db import models

# Source Schema Models
class Websites(models.Model):
    website_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500, null=False)
    raw_content = models.TextField(null=False)
    scraped_at = models.DateTimeField(null=False, auto_now_add=True)
    language = models.CharField(max_length=50, null=False)

    #? Meta data about your DB
    class Meta:
        db_table = 'Source.website'

class ENewspapers(models.Model):
    e_newspaper_id = models.AutoField(primary_key=True)
    image_path = models.CharField(max_length=500, null=False)
    raw_text = models.TextField(null=False)
    scanned_at = models.DateTimeField(null=False, auto_now_add=True)
    edition = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Source.e-newspaper'

class YouTubeVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_url = models.CharField(max_length=500, null=False)
    transcript = models.TextField(null=False)
    downloaded_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        db_table = 'Source.video'

# Processed_and_analyzed Schema Models
class ProcessedWebsites(models.Model):
    processed_website_id = models.AutoField(primary_key=True)
    processed_content = models.TextField(null=False)
    sentiment = models.CharField(max_length=10, choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], null=False)
    processed_at = models.DateTimeField(null=False, auto_now_add=True)
    #! Conflict
    source_website = models.ForeignKey(Websites, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Processed_and_analyzed.processed_website'

class ProcessedENewspapers(models.Model):
    processed_e_newspaper_id = models.AutoField(primary_key=True)
    processed_text = models.CharField(max_length=255, null=False)
    sentiment = models.CharField(max_length=10, choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], null=False)
    processed_at = models.DateTimeField(null=False, auto_now_add=True)
    #!Conflict
    source_e_newspaper = models.ForeignKey(ENewspapers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Processed_and_analyzed.processed_e_newspaper'

class ProcessedYouTubeVideos(models.Model):
    processed_video_id = models.AutoField(primary_key=True)
    sentiment = models.CharField(max_length=10, choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], null=False)
    processed_transcript = models.TextField(null=False)
    processed_at = models.DateTimeField(null=False, auto_now_add=True)
    #! Conflict
    source_video = models.ForeignKey(YouTubeVideos, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Processed_and_analyzed.processed_video'

# Notification Schema Models
class PIBOfficials(models.Model):
    official_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    contact_detail = models.JSONField(null=False)
    department = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Notification.pib_official'

class NotificationsLog(models.Model):
    notification_id = models.AutoField(primary_key=True)
    official_id = models.ForeignKey(PIBOfficials, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=10, choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], null=False)
    message = models.TextField(null=False)
    sent_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        db_table = 'Notification.notification_log'
