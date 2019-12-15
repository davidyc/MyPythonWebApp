from django.db import models

# Create your models here.
class Player(models.Model):
    image = models.ImageField(upload_to="image/")
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Section(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Theme(models.Model):
    title = models.CharField(max_length=25)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Phase(models.Model):
    number = models.IntegerField()
    startDate = models.DateField()
    finishDate = models.DateField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return "Phase {} {} ".format(str(self.number),self.theme.title)