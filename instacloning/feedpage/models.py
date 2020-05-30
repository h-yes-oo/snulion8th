from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(blank = True, upload_to = 'feed_photos')

    def __str__(self):
        return self.title

class Feedcomment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)