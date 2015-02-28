from django.db import models

class User_Detail(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    profile_pic = models.CharField(max_length = 100)

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date_posted = models.DateTimeField()
    date_due = models.DateTimeField()
    status = models.BooleanField(default = False)
