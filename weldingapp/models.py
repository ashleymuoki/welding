from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from welderapp.models import Design

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item = models.CharField(max_length=40)
    length_feet = models.IntegerField()
    height_feet = models.IntegerField()
    cost = models.IntegerField()
    design = models.FileField()
    def __str__(self):
        return self.item

class Orderitem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitem)
    ordered = models.BooleanField(default=False)
    date_of_order = models.DateTimeField(default=timezone.now)
    date_of_completion = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username





















