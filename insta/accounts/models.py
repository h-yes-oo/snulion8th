from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User   # 추가
from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver 

...
class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):   # 추가
        return 'id=%d, user_id=%d' % (self.id, self.user.id)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
