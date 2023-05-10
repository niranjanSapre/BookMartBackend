from django.db import models
from django.contrib.auth.models import User
from sell.models import Book_Detail

# Create your models here.

class Order_Summary(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=255)
    buyer_mobile_no = models.BigIntegerField()
    buyer_country = models.CharField(max_length=255)
    buyer_state = models.CharField(max_length=255)
    buyer_city = models.CharField(max_length=255)
    buyer_postal_code = models.CharField(max_length=100)
    buyer_address = models.TextField()
    book = models.ForeignKey(Book_Detail, on_delete=models.CASCADE, null=True)
    total_amount = models.FloatField(null=True)
    purchase_date = models.DateField(null=True)
    delivery_status = models.CharField(max_length=100)

class Payment_Detail(models.Model):
    invoice_number = models.CharField(max_length=255)
    transaction_date = models.DateField()
    book = models.ForeignKey(Book_Detail, on_delete=models.CASCADE, null=True)
    book_name = models.CharField(max_length=255, null=True)
    book_price = models.FloatField()
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=100, null=True)
    receipt_number = models.BigIntegerField()
    billing_email = models.CharField(max_length=255)
    billing_address = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
