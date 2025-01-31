from django.db import models


from django.contrib.auth.models import AbstractUser

# Create your models here.



class CpUser(AbstractUser):
	CodeForcesID = models.CharField(max_length=100,unique = True)
	CodeChefID = models.CharField(max_length=100, blank= True)
	LeetCodeID = models.CharField(max_length=100,null=True,unique = True)
	AtCoderID = models.CharField(max_length=100,null=True,unique = True,blank=True)
	SpojID = models.CharField(max_length=100,null=True,unique = True,blank=True)




