from django.db import models
from sell.models import Book_Detail
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='sender')
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='receiver')
    message_status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)