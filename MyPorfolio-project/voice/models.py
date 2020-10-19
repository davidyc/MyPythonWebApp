from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=30)  

    def __str__(self):
        return "Кандидат {}".format(self.name)

class Voice(models.Model):
    name = models.CharField(max_length=50)  
    level = models.CharField(max_length=25, default="Не указан")  
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{} проголосовал за {}".format(self.name, self.candidate.name)