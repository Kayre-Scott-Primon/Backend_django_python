from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name