from django.db import models

#? Create ORMs here
class Website(models.Model):
    website_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    raw_content = models.TextField()
    scraped_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'Source.website'
