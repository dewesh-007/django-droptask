from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Tasklist(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
