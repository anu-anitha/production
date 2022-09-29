from django.db import models

# Create your models here.
class school(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	age=models.IntegerField()
	city=models.CharField(max_length=100)