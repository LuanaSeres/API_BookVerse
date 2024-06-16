from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Define um novo modelo chamado Wishlist (Lista de Desejos)
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    # Define o método especial __str__ que retorna o título do livro quando o objeto é representado como string
    def __str__(self):
        return self.title
