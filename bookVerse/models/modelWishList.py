from django.contrib.auth.models import User
from django.db import models
from ..models.modelBook import Book

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    book = models.ManyToManyField(Book, related_name='wishlisted_by')
    priority = models.IntegerField()

    def __str__(self):
        return self.user.username