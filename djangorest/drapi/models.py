from django.db import models

# Create your models here.
class demo(models.Model):
    Name = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    course_duration =models.IntegerField()
    seat=models.IntegerField()