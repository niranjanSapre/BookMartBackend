from django.urls import path
from .views import WishlistView, UserUploadedWishlistView, WishlistDeleteView, UserWishlistDelete

urlpatterns = [
    path('', WishlistView.as_view()),
    path('userwishlist', UserUploadedWishlistView.as_view()),
    path('<int:id>', WishlistDeleteView.as_view()),
    path('deletewishlist', UserWishlistDelete.as_view())
]