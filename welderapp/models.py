from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Welder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    welder_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    cover = models.FileField()
    def __str__(self):
        return self.welder_name


class Design(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_name = models.CharField(max_length=50)
    desc = models.TextField()
    cost = models.IntegerField()
    picture = models.FileField()

    def __str__(self):
        return self.design_name




