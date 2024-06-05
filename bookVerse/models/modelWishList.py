from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Default Title')
    author = models.CharField(max_length=255, default='Default Author')  # Defina um valor padrão
    genre = models.CharField(max_length=100, default='Default Genre')  # Defina um valor padrão
    description = models.TextField(default='No description')  # Defina um valor padrão
    priority = models.IntegerField(default=0, null=True, blank=True)

    def _str_(self):
        return self.title