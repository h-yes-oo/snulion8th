from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User 
from django.db.models.signals import post_save  
from django.dispatch import receiver   

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank = True, null=True)
    
    def __str__(self):   # 추가
        return 'id=%d, user_id=%d' % (self.id, self.user.id)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()

def seed_user_profile():
        myfake = Faker('ko_KR')
        myfake2 = Faker('en') 
        
        for i in range(20):
            username = myfake.simple_profile()['username']
            user = User.objects.create_user(username=username, password='123')
            email = myfake.free_email()
            birthday = myfake.date_of_birth()

            Profile.objects.filter(user=user).update(email=email, birthday=birthday)
        
