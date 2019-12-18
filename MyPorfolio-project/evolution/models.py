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
    done = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Phase(models.Model):
    number = models.IntegerField(unique=True)
    startDate = models.DateField()
    finishDate = models.DateField()    
    
    def __str__(self):
        return "Phase {} {}-{} ".format(str(self.number),str(self.startDate), str(self.finishDate))

class PhaseTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
   
    def __str__(self):
        return "{} {} ".format(str(self.phase),self.theme)



class _phase():
    def __init__(self, name):
        self.name = name
        self.themes = list()

class _theme():
    def __init__(self, name):
        self.name = name
        self.themes = list()