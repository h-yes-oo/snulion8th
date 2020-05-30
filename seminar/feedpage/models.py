from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User


class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User, blank=True, related_name='like_feeds', through='Like')

    def update_date(self):  # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            Feed.objects.create(
                title=myfake.bs(),
                content=myfake.text()
            )


class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User, blank=True, related_name='like_feedcomments', through='LikeComment')

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedcomment = models.ForeignKey(FeedComment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
