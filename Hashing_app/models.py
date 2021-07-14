from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    #portfolio_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    first_name = models.CharField(max_length=20),
    last_name = models.CharField(max_length=20),
    #email = models.EmailField(max_length=40),
    address = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.user.username
