from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User   
from django.db.models.signals import post_save  
from django.dispatch import receiver   
...
class Profile(models.Model):  
    '''
        User model과 연결 - 1 to 1 mapping
        User <-> Profile
        1) user1.profile
        2) Profile1.user

    ''' 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank = True, null=True)
    address = models.CharField(max_length=100, blank = True)

    follows = models.ManyToManyField('self', through = 'Follow', \
            blank=True, related_name = 'followed', symmetrical=False)

    def __str__(self):   
        ''' 
        string fommatting 
        return 'id=%d, user_id=%d, college=%s, major=%s' \
                % (self.id, self.user.id, self.college, self.major)
        '''
        return f'id={self.id}, user_id={self.user.id}, \
                college={self.college}, major={self.major}, \
                email={self.email}, birthday = {self.birthday}, \
                address={self.address}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
    '''
        seed(user) 함수
        shell에서 user = User.objects.get(id = id) 후에
        Profile.seed(user)를 통해서 profile을 임의로 할당 가능.
    '''
    def seed_user_profile():
        myfake = Faker('ko_KR')
        myfake2 = Faker('en') # 미국대학 이름을 위한 faker!
        
        for i in range(20):
            username = myfake.simple_profile()['username']
            user = User.objects.create_user(username=username, password='123')

            college = myfake2.state() 
            major = myfake.catch_phrase()
            email = myfake.free_email()
            birthday = myfake.date_of_birth()
            address = myfake.address()

            Profile.objects.filter(user=user).update(college=college,\
                major=major, email=email, birthday=birthday, address=address)
        

class Follow(models.Model): 
    # 서로 연결해주기 위해서는 related_name이 반대되는 것이어야 한다. 
    follow_to = models.ForeignKey(Profile, related_name = 'follow_from', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(Profile, related_name = 'follow_to', on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', through = 'Follow', blank=True, \
                                        related_name = 'followed', symmetrical=False)
                                        # symmetrical이 true일 때에는 양방향으로 모두 친구여야한다. 
                                        # 여기서는 단방향이 가능하므로 false로 설정
    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)
