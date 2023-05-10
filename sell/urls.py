from django.urls import path
from .views import BookDetailsList, BookDetailsView, AllBooksView, UserUploadedBooksView, BookEstimatedPriceView, BookImageSaveView, BookImageDeleteView

urlpatterns = [
    path('', BookDetailsList.as_view()),
    path('all', AllBooksView.as_view()),
    path('<int:id>', BookDetailsView.as_view()),
    path('userupload', UserUploadedBooksView.as_view()),
    path('estprice', BookEstimatedPriceView.as_view()),
    path('bookimage', BookImageSaveView.as_view()),
    path('imagedelete/<int:id>', BookImageDeleteView.as_view())
]