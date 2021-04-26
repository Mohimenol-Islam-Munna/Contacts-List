from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.full_name
