from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from bookVerse.views.viewBook import *
from bookVerse.views.viewReview import *
from bookVerse.views.viewWishList import *
from bookVerse.views.viewReadingStatus import *
from bookVerse.views.viewUser import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Book
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Review
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),

    # WishList
    path('wishlist/', WishListView.as_view(), name='wishlist-list'),
    path('wishlist/create/', WishlistCreateView.as_view(), name='wishlist-create'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/<int:pk>/update/', WishlistUpdateView.as_view(), name='wishlist-update'),
    path('wishlist/<int:pk>/delete/', WishlistDeleteView.as_view(), name='wishlist-delete'),

    # Reading Status
    path('reading-status/', ReadingStatusListView.as_view(), name='reading-status-list'),
    path('reading-status/create/', ReadingStatusCreateView.as_view(), name='reading-status-create'),
    path('reading-status/<int:pk>/', ReadingStatusDetailView.as_view(), name='reading-status-detail'),
    path('reading-status/<int:pk>/update/', ReadingStatusUpdateView.as_view(), name='reading-status-update'),
    path('reading-status/<int:pk>/delete/', ReadingStatusDeleteView.as_view(), name='reading-status-delete'),

    # User
    path('users/', UserList.as_view(), name='user_list'),
    path('users/generate/', UserGenerate.as_view(), name='user_generate'),
    path('users/edit/<int:id>/', UserEdit.as_view(), name='user_edit'),
    path('users/delete/<int:id>/', UserDelete.as_view(), name='user_delete'),
]
