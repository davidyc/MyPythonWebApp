from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="image/")
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, default="No description")
    adddate = models.DateField(auto_now=True)
    shortname = models.CharField(max_length=10, default="")


    def __srt__(self):
        return self.summary