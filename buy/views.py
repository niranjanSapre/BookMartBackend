from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BuyDetailsSerializer, PaymentDetailsSerializer
from rest_framework import permissions
from .models import Order_Summary, Payment_Detail
from sell.models import Book_Detail
from rest_framework.response import Response
# Create your views here.

class BuyDetailsList(ListCreateAPIView):
    serializer_class = BuyDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        book_id = self.request.POST.get('book')
        book = Book_Detail.objects.get(id=book_id)
        serializer.save(user=self.request.user, book=book)

    def get_queryset(self):
        return Order_Summary.objects.filter(user=self.request.user)
    
class UserBuyDetailsView(ListCreateAPIView):

    serializer_class = BuyDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Order_Summary.objects.filter(user=self.request.user)
    
class PaymentDetails(ListCreateAPIView):
    serializer_class = PaymentDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        book_id = self.request.POST.get('book')
        book = Book_Detail.objects.get(id=book_id)
        book.status = "Sold"
        book.save()
        serializer.save(user=self.request.user, book=book)

    def get_queryset(self):
        return Payment_Detail.objects.filter(user=self.request.user)
    
class UserPaymentDetails(ListCreateAPIView):
    serializer_class = PaymentDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Payment_Detail.objects.filter(user=self.request.user)
    