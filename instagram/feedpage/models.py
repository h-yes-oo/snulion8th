from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Feed(models.Model):
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='feed_photos')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):   # 추가
        return 'id=%d, user_id=%d, content=%s' % (self.id, self.user.id, self.content)

        
class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete = models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)