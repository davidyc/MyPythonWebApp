from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="image/")
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, default="No description")
    adddate = models.DateField(auto_now=True)
    shortname = models.CharField(max_length=10, default="")
    externalurl = models.CharField(max_length=200, default="Internal deploy", null=True)
    isexrernalurl = models.BooleanField(default = False)


    def __srt__(self):
        return self.summary

class Developer(models.Model):
    image = models.ImageField(upload_to="image/photos")
    name = models.CharField(max_length=50)
    borndate = models.DateField()
    company = models.CharField(max_length=50)
    postion = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
