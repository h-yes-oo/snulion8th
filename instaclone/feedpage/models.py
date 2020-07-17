from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.
class Feed(models.Model): 
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    #author=models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
    photo = models.ImageField(blank=True, upload_to='feed_photos')
    
    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.id

class FeedComment(models.Model):
    comment=models.TextField()
    feed=models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)