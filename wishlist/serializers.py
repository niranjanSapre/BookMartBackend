from rest_framework.serializers import ModelSerializer
from .models import Wishlist

class WishlistSerializer(ModelSerializer):

    class Meta:
        model = Wishlist
        depth = 2
        fields = '__all__' 