from django.contrib import admin
from django.urls import path
from bookVerse.views.viewBook import *
from bookVerse.views.viewReview import *
from bookVerse.views.viewWishList import WishListView, WishlistDetailView
from bookVerse.views.viewReadingStatus import ReadingStatusView, ReadingStatusDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('api/wishlist/', WishListView.as_view(), name='wishlist'),
    path('api/wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('api/reading-status/', ReadingStatusView.as_view(), name='reading-status'),
    path('api/reading-status/<int:pk>/', ReadingStatusDetailView.as_view(), name='reading-status-detail'),
]
