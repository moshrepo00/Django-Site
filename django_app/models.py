from django.db import models

# Create your models here.
class Athlete(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)


class Coach(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team)
