from rest_framework.serializers import ModelSerializer
from .models import Order_Summary, Payment_Detail

class BuyDetailsSerializer(ModelSerializer):

    class Meta:
        model = Order_Summary
        depth = 2
        fields = '__all__' 

class PaymentDetailsSerializer(ModelSerializer):

    class Meta:
        model = Payment_Detail
        depth = 1
        fields = '__all__'