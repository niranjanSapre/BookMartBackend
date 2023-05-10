from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book_Detail(models.Model):
    def nameFile(instance, filename):
        user = User.objects.get(username=instance.user)
        return '/'.join([str(user.username), filename])

    book_isbn = models.CharField(max_length=15)
    book_name = models.CharField(max_length=255)
    book_page = models.IntegerField()
    book_medium = models.CharField(max_length=20)
    book_author = models.CharField(max_length=255)
    book_genre = models.CharField(max_length=255)
    book_cover_page = models.ImageField(upload_to=nameFile, blank=True)
    book_last_page = models.ImageField(upload_to=nameFile, blank=True)
    book_page1 = models.ImageField(upload_to=nameFile, blank=True)
    book_page2 = models.ImageField(upload_to=nameFile, blank=True)
    book_page3 = models.ImageField(upload_to=nameFile, blank=True)
    book_price = models.FloatField()
    book_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=45)
    posted_date = models.DateField(null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

class Book_Images(models.Model):
    def nameFile(instance, filename):
        user = User.objects.get(username=instance.user)
        return '/'.join([str(user.username)+'imageprocessing', filename])

    book_page1 = models.ImageField(upload_to=nameFile, blank=True)
    book_page2 = models.ImageField(upload_to=nameFile, blank=True)
    book_page3 = models.ImageField(upload_to=nameFile, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.FloatField(null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)