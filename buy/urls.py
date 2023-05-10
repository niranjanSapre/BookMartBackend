from django.urls import path
from .views import BuyDetailsList, UserBuyDetailsView, PaymentDetails, UserPaymentDetails

urlpatterns = [
    path('', BuyDetailsList.as_view()),
    path('userorder', UserBuyDetailsView.as_view()),
    path('paymentdetails', PaymentDetails.as_view()),
    path('userpayment', UserPaymentDetails.as_view()),
]