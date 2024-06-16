from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from ..models.modelBook import Book


# Define um novo modelo chamado Review (Revisão)
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

    # Define o método especial __str__ que retorna uma string representando a revisão
    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
