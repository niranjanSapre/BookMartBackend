from django.urls import path
from .views import RegisterView, LoginView, DeleteAccountView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('deleteaccount/<int:id>', DeleteAccountView.as_view())
]