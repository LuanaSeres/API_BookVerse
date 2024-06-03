from django.contrib.auth.models import User
from django.db import models
from ..models.modelBook import Book

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    books = models.ManyToManyField(Book, related_name='wishlisted_by')

    def __str__(self):
        return self.user.username