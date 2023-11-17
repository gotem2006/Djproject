from django.db import models

# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    # basket_history = models.JSONField()
    adress = models.CharField(max_length=256)
    pass