from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.BigIntegerField()
    message=models.TextField(null=True,blank=True)

def __str__(self):
        return self.name 
