from django.contrib import admin
from django.urls import path
from bookVerse.views.viewBook import BookListView, BookDetailView
from bookVerse.views.viewReview import ReviewListView, ReviewDetailView
from bookVerse.views.viewWishList import WishListView, WishlistDetailView
from bookVerse.views.viewReadingStatus import ReadingStatusView, ReadingStatusDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/comments/', ReviewListView.as_view(), name='review-list-create'),
    path('api/comments/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('api/wishlist/', WishListView.as_view(), name='wishlist'),
    path('api/wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('api/reading-status/', ReadingStatusView.as_view(), name='reading-status'),
    path('api/reading-status/<int:pk>/', ReadingStatusDetailView.as_view(), name='reading-status-detail'),
]
