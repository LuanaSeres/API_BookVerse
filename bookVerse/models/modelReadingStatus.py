from django.contrib.auth.models import User
from django.db import models
from ..models.modelBook import Book

# Define um novo modelo chamado ReadingStatus (Status de Leitura)
class ReadingStatus(models.Model):
    # Define uma lista de opções para o campo status
    STATUS_CHOICES = [
        ('read', 'Read'),       # Opcion para livros lidos
        ('unread', 'Unread'),   # Opcion para livros não lidos
        ('reading', 'Reading'), # Opcion para livros em leitura
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_statuses')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    progress = models.IntegerField(default=0)

    # Define o método especial __str__ que retorna uma string representando o estado de leitura
    def _str_(self):
        return f'{self.user.username} - {self.book.title} - {self.status}'
