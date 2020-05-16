from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User   
from django.db.models.signals import post_save  
from django.dispatch import receiver   
...
class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''
        User model과 연결 - ono to one mapping
        User <-> Profile
        1) user1.profile
        2) Profile1.user

    '''
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)

    def __str__(self):   
        # string fommatting 
        # return 'id=%d, user_id=%d, college=%s, major=%s' % (self.id, self.user.id, self.college, self.major)
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()