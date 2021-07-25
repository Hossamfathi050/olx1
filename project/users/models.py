
from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=250)
    email= models.EmailField( max_length=254)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=75)
    website = models.CharField(max_length=75)
    twitter = models.CharField(max_length=75)
    instgram = models.CharField(max_length=75)
    facebook = models.CharField(max_length=75)

    def __str__(self):
        return self.fullname
        
