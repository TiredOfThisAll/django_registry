from django.db import models

class Registry(models.Model):
    abc = models.IntegerField()
    start = models.BigIntegerField()
    end = models.BigIntegerField()
    capacity = models.BigIntegerField()
    operator = models.CharField(max_length=200)
    region = models.CharField(max_length=3000)
    GAR_territory = models.CharField(max_length=3000)
    TIN = models.CharField(max_length=200)
