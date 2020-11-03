from django.db import models

# Create your models here.
class Member(models.Model):
    surname = models.CharField(max_length=100) # Name of the member
    firstname = models.CharField(max_length=100) # Firstname of the member