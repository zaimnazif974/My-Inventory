from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    ammount = models.IntegerField()
    description = models.TextField()
    effect = models.CharField(max_length=100,default='')
    category = models.CharField(max_length=100,default='')
