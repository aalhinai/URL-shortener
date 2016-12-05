# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# table named ‘User_Urls’ in our database with the following field:
#
# short_id (it will store short URL id), (It is of max_length 15 and it is a primary key)
# httpurl (it will store URL), (It is of max_length 200)
# pub_date (It will store the date and time)
# count (It will store the number of times the URL is visited)

class Usr_Urls(models.Model):
      short_id = models.SlugField(max_length=8,primary_key=True)
      httpurl = models.URLField(max_length=200)
      pub_date = models.DateTimeField(auto_now=True)
      count = models.IntegerField(default=0)
      #user = models.OneToOneField(User, on_delete=models.CASCADE, default='User')
      #user = models.ForeignKey(User, on_delete=models.CASCADE, default= 'User')
      user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='User')

def __str__(self):
    return self.httpurl
