from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(default=date.today)  # ✅ Fix: Set default to current date

    def __str__(self):
        return self.name