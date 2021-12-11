from django.db import models
from django import forms 


# Create your models here.
class EmailModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    emailadress = models.CharField( max_length=50)
    fullname =models.CharField( max_length= 100)


    def __str__(self) -> str:
        return self.emailadress
    dbTableForEmail = models.Manager()
