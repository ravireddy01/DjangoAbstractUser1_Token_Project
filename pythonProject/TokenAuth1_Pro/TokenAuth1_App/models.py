from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=(('m', 'M'), ('f', 'F'), ('o', 'O')))

    def __str__(self):
        return self.gender

    # def __str__(self):
    #     return str(self.age) if self.age else ''
    #


