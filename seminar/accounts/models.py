from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    birth = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=20, blank=True)
    
    follows = models.ManyToManyField('self', through = 'Follow', blank=True, related_name = 'followed', symmetrical=False)

    def __str__(self):   # 추가
        return 'id=%d, user_id=%d, college=%s, major=%s, birth=%s, email=%s' % (self.id, self.user.id, self.college, self.major, self.birth, self.email)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:      
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()


class Follow(models.Model):
    follow_from = models.ForeignKey(Profile, related_name = 'follow_to', on_delete=models.CASCADE)
    follow_to = models.ForeignKey(Profile, related_name = 'follow_from', on_delete=models.CASCADE)

    def __str__(self):
        return '{}follows{}'.format(self.follow_from, self.follow_to)