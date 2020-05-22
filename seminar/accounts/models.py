from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20,  blank=True)
    major = models.CharField(max_length=20, blank=True)
    birthday = models.CharField(max_length=8,null=True, blank=True)

def __str__(self):
    return 'id-%d, user_id=%d, college=%s, major=%s, birthday=%s' % (self.id, self.user.id, self.college, self.major, self.birthday)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()