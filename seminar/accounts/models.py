from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User   # 추가

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    birthdate = models.CharField(max_length=20, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    follows = models.ManyToManyField("self", through = "Follow", blank=True, related_name = 'followed', symmetrical=False)##symemetrical이 true일 시 서로 팔로우됨

    def __str__(self):   # 추가
        return 'id=%d, user_id=%d, college=%s, major=%s birthdate=%s, contact=%s' % (self.id, self.user.id, self.college, self.major, self.birthdate, self.contact)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
    
    
    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            user = User.objects.create_user(
                username=myfake.user_name(),
                password=myfake.ssn())
            profile = user.profile
            profile.college=myfake.borough()
            profile.major=myfake.job()
            profile.birthdate=myfake.date_of_birth()
            profile.contact=myfake.phone_number()
            user.save()
            # auth.login(request, user)
            

class Follow(models.Model): 
    follow_to = models.ForeignKey(Profile, related_name = 'follow_from', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(Profile, related_name = 'follow_to', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)


