from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=12)
    created_at = models.DateTimeField()
    favourite = models.BooleanField(default=False)
    Choices = [
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Personal', 'Personal'),
    ]

    type = models.CharField(max_length = 20, choices=Choices)