from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chat 
from .serializers import ChatSerializer
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User

# Create your views here.

class MessageSendView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        receiver_id = self.request.POST.get('receiver')
        receiver = User.objects.get(id=receiver_id)
        sender_id = self.request.POST.get('sender')
        sender = User.objects.get(id=sender_id)
        serializer.save(sender=sender, receiver=receiver)

    def get_queryset(self):
        print(self.request.user)
        return Chat.objects.filter(sender=self.request.user)
    
class MessageReceiveView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        changeStatus = Chat.objects.filter(receiver=self.request.user)
        for item in changeStatus:
            item.message_status = True
            item.save()
        return Chat.objects.filter(receiver=self.request.user)
    
class MessageOnlyReceiveView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(receiver=self.request.user)


class MessageAllView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(sender=self.request.user)

class PreviousMessageView(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        receiver_id = self.request.POST.get('receiver')
        receiver = User.objects.get(id=receiver_id)
        sender_id = self.request.POST.get('sender')
        sender = User.objects.get(id=sender_id)
        return Chat.objects.filter(sender=sender, receiver=receiver)