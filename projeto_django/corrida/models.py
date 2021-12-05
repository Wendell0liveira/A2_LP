from django.db import models

# Create your models here.

class Race(models.Model):
    begin = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)

    def __str__(self):
        return self.begin+" to "+self.end