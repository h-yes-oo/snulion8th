from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User  
from django.db.models.signals import post_save 
from django.dispatch import receiver  

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    follows = models.ManyToManyField('self',through = 'Follow', blank=True, related_name='followed',symmetrical=False)

    def seed(count): 
        myfake = Faker()
        for i in range(count):
            user=User.objects.create_user(username=myfake.name(),password=1234)
            user.profile.college=myfake.name()
            user.profile.major=myfake.name()
            user.profile.save()


    def __str__(self):  
        return 'id=%d, user_id=%d, college=%s, major=%s' % (self.id, self.user.id, self.college, self.major)
        # 아래 코드와 동일함
        # return 'id=' + self.id + 'user_id=' + self.user.id + ', ' + 'college=' + self.college + ', ' + 'major=' + self.major

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

class Follow(models.Model):
    follow_to = models.ForeignKey(Profile, related_name = 'follow_from', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(Profile, related_name = 'follow_to', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)