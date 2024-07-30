from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.phone}"
