from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Wishlist 
from rest_framework import permissions
from sell.models import Book_Detail
from .serializers import WishlistSerializer
from rest_framework.response import Response

# Create your views here.

class WishlistView(ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        book_id = self.request.POST.get('book')
        book = Book_Detail.objects.get(id=book_id)

        serializer.save(user=self.request.user, book=book)

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    
class UserUploadedWishlistView(ListCreateAPIView):

    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    
# class UserCurrentBookWishlistView(ListCreateAPIView):

#     serializer_class = WishlistSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def get_queryset(self):
#         return Wishlist.objects.filter(user=self.request.user)
    
class WishlistDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    

class UserWishlistDelete(ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        Wishlist.objects.filter(user=self.request.user, status="unliked").delete()
        return Wishlist.objects.filter(user=self.request.user)