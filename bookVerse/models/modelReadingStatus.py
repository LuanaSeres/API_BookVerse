from django.contrib.auth.models import User
from django.db import models
from ..models.modelBook import Book

class ReadingStatus(models.Model):
    STATUS_CHOICES = [
        ('read', 'Read'),
        ('unread', 'Unread'),
        ('reading', 'Reading'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_statuses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    progress = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.user.username} - {self.book.title} - {self.status}'