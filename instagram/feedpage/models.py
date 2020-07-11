from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Feed(models.Model): 
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds',through='Like')
    photo = models.ImageField(blank=True, upload_to='feed_photos')

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FeedComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_comments', through='CommentLike')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(FeedComment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
