from django.db import models

# Create your models here.
class Ad(models.Model):
    name = models.CharField(max_length=50)
    price=models.IntegerField()
    content=models.TextField()
 
    def __str__(self):
        return self.name
        

