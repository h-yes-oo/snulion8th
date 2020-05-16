from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver   # 추가

# Create your models here.
class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)

    def __str__(self):   # 추가
        return 'id=%d, user_id=%d, college=%s, major=%s' % (self.id, self.user.id, self.college, self.major)
        # return f'id={self.id}, user_id={sefl.user_id}, college={self.college}, major={self.major}'
        # 아래 코드와 동일함
        # return 'id=' + self.id + 'user_id=' + self.user.id + ', ' + 'college=' + self.college + ', ' + 'major=' + self.major

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

