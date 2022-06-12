from django.db import models

# Create your models here.

class User(models.Model):
    e_id = models.CharField(max_length=100)
    e_name = models.CharField(max_length=100)
    e_email = models.EmailField()

    def __str__(self):
        return self.e_name



