from django.db import models
from django.utils import timezone

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def update_title(self, title):
        self.title = title
        self.save()
    
    def update_content(self, content):
        self.content = content
        self.save()