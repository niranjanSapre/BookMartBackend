from django.db import models
from django.contrib.auth.models import User
from sell.models import Book_Detail

# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book_Detail, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, null=True)