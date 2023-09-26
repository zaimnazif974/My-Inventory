from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    ammount = models.IntegerField()
    description = models.TextField()
    effect = models.CharField(max_length=100, default= 'None')
    category = models.CharField(max_length=100, default= 'Unknown')
