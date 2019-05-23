from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlparse

# Create your models here.


class ProfileOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='No_name_added')
    age = models.PositiveIntegerField(default=0)
    description = models.TextField(default='No_description')
    picture = models.URLField(default='https://www.tenforums.com/geek/gars/images/2/types/thumb__ser.png')


    def __str__(self):
        return f"{self.user}"



