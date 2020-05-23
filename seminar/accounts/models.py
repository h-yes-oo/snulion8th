from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    mbti = models.CharField(max_length=4, blank=True)
    def __str__(self):   
        return 'id=%d, user_id=%d, college=%s, major=%s, mbti=%s' % (self.id, self.user.id, self.college, self.major,self.mbti)
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

    def seed(count): # 추가
        myfake = Faker()
        for i in range(count):
            user = User.objects.create_user(username=myfake.name(), password=myfake.password())
            profile=user.profile
            profile.college=myfake.words()[0][:3]
            profile.major=myfake.words()[0][:3]
            profile.mbti=myfake.words()[0][:4]
            profile.save()