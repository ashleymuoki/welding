from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=30)
    date_of_order = models.DateTimeField(default=timezone.now)
    date_of_completion = models.DateField()
    cover = models.FileField()

    def __str__(self):
        return self.client_name


class Item(models.Model):
    client_name = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=40)
    length_feet = models.IntegerField()
    height_feet = models.IntegerField()
    cost = models.IntegerField()
    design = models.FileField()

    def __str__(self):
        return self.item_name



















