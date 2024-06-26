from django.contrib.auth.models import User
from django.db import models

# Define um novo modelo chamado Book (Livro)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', default=1)

    # Define o método especial __str__ que retorna o título do livro quando o objeto é representado como string
    def _str_(self):
      return self.title
