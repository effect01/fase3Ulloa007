from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.




class Profile(models.Model):
    CODES_PHONE = (
        (56, 'CHL +56'),
        (54,'ARG +54'),
        (55,'BRZ +55'),
        (1,'USA +1'),
        (57,'COL +57'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    points = models.IntegerField( default=0)
    code_number = models.IntegerField( choices=CODES_PHONE, default=CODES_PHONE[0][0]) 
    phone_number = models.IntegerField( default=0)
    dateBirth = models.DateField()
    def __str__(self):
        return "%s" % (self.user)
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    def pointProfileCount(self):
        return self.profilevote_set.all().count()
    def pointProfileMedia(self):
        star2=0
        for star in self.profilevote_set.all():
            star2= star2+ round(float(star.vote),1)
        if star2 != 0:
            return star2/self.pointProfileCount()
        else:
            return 0
    def pointProfileMediaPercent(self):
        if self.pointProfileMedia() != 0:      
            return round( self.pointProfileMedia()*20)
        else:
            return 0
    def countryProfile(self):
        CODES_PHONE ={ 56: 'CHILE' , 1 : 'USA',  54: 'ARGENTINA', 55: 'BRAZIL', 57:'COLOMBIA'}
        return CODES_PHONE[self.code_number]
    def ex1(self):
        if(self.user.userbook_set.all().first()):
            return  True
        return False
    def birthday(self):
        return self.dateBirth
    def igotttem(self):
        return self.user.username


class ProfileVote(models.Model):
    VOTE_POINT = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    vote = models.IntegerField( choices=VOTE_POINT )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        constraints = [  models.UniqueConstraint(fields=['user', 'profile'], name='1 user, 1 vote to profile ')]
    def __str__(self):
        return "User: %s, Vote to: %s / %s" % (self.user, self.profile, self.vote)
