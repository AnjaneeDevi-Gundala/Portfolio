from django.db import models

# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=50)
    company = models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=220)
    message=models.CharField(max_length=1000)
    

