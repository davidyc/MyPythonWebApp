from django.db import models

# Create your models here.
class Player(models.Model):
    image = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=25)

class Section(models.Model):
    title = models.CharField(max_length=25)

class Theme(models.Model):
    title = models.CharField(max_length=25)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

class Phase(models.Model):
    number = models.IntegerField()
    startDate = models.DateField(auto_now=True)
    finishDate = models.DateField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)