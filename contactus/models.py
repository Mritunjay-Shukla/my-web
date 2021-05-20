from django.db import models

# Create your models here.

class Contactus(models.Model):

    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=99)
    description = models.TextField(default=None)

    def __str__(self):
        return f"{self.name} asking for { self.subject }"
