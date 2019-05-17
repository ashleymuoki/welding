from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Demand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(default=timezone.now)
    cover = models.FileField()

    def __str__(self):
        return self.user.username


class Design(models.Model):
    name = models.ForeignKey(Demand, on_delete=models.CASCADE)
    item = models.CharField(max_length=40)
    length_feet = models.IntegerField()
    height_feet = models.IntegerField()
    cost = models.IntegerField()
    design = models.FileField()

    def __str__(self):
        return self.item






