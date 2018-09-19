from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)              
    email = models.EmailField(max_length=70,blank=True)
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile=UserProfile.objects.create(user=kwargs['instance'])
        post_save.connect(create_profile,sender=User)

class driving(models.Model):
    JAMMU= 'JM'
    DELHI = 'DL'
    MUMBAI = 'MB'
    choose_city= (
        (JAMMU, 'Jmmu'),
        (DELHI, 'Delhi'),
        (MUMBAI, 'Mumbai'),
        )
    city=models.CharField(choices=choose_city, default=JAMMU, max_length=2)
    area=models.CharField(max_length=150,default='')
    name=models.CharField(max_length=200,default='')


    
    

  
 

