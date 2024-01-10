from django.db import models

# Create your models here.


class Order(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    # basket_history = models.JSONField()
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=50)
    