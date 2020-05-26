from django.db import models
# Create your models here.
from django.utils import timezone # 장고는 created_at과 updated_at을 알아서 만들어 주지 않음. id는 만들어 줌
from faker import Faker 
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model): # 모델 클래스명은 단수형을 사용 (Feeds(x) Feed(O))
    # id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete= models.CASCADE)    
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds', through='Like')    

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            Feed.objects.create(title=myfake.bs(), content=myfake.text())

    def __str__(self):
        return self.title

class FeedComment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_comments', through='CommentLike')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    # feed comment와 feed 연결로 feed가 삭제되는 경우에 댓글들로 다 삭제되도록,
    # => on_delete = models,CASCADE를 해준다. ㅎㅅㅎ
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