from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)  # Corrected here
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}"
