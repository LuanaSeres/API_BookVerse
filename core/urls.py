from django.contrib import admin
from django.urls import path
from bookVerse.views.viewBook import *
from bookVerse.views.viewReview import *
from bookVerse.views.viewWishList import *
from bookVerse.views.viewReadingStatus import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('wishlist/', WishListView.as_view(), name='wishlist-list'),
    path('wishlist/create/', WishlistCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/<int:pk>/update/', WishlistUpdateView.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', WishlistDeleteView.as_view(), name='wishlist-delete'),
    path('reading-status/', ReadingStatusListView.as_view(), name='reading-status-list'),
    path('reading-status/create/', ReadingStatusCreateView.as_view(), name='reading-status-create'),
    path('reading-status/<int:pk>/', ReadingStatusDetailView.as_view(), name='reading-status-detail'),
    path('reading-status/<int:pk>/update/', ReadingStatusUpdateView.as_view(), name='reading-status-update'),
    path('reading-status/<int:pk>/delete/', ReadingStatusDeleteView.as_view(), name='reading-status-delete'),

]
