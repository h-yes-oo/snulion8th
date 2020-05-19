from django.db import models

# Create your models here.
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User   # 추가
from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver   # 추가

...
class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

    def get_major(self):
        return self.major
    
    def get_college(self):
        return f'college= {self.college}'