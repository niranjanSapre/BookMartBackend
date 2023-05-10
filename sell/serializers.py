from rest_framework.serializers import ModelSerializer
from .models import Book_Detail, Book_Images

class BookDetailsSerializer(ModelSerializer):

    class Meta:
        model = Book_Detail
        depth = 1
        fields = '__all__' 

class BookImageSerializer(ModelSerializer):

    class Meta:
        model = Book_Images
        fields = '__all__'