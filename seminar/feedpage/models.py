from django.db import models
from django.utils import timezone
from faker import Faker


class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

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
