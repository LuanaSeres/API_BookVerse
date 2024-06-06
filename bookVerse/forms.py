from django import forms
from .models.modelBook import Book
from .models.modelReview import Review
from .models.modelWishList import Wishlist
from django.contrib.auth.models import User
from .models.modelReadingStatus import ReadingStatus

# Formulário para o modelo Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description']  # Campos do modelo Book que serão incluídos no formulário

# Formulário para o modelo Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Campos do modelo Review que serão incluídos no formulário

# Formulário para o modelo Wishlist
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'author', 'genre', 'description', 'priority']  # Campos do modelo Wishlist que serão incluídos no formulário

# Formulário para o modelo ReadingStatus
class ReadingStatusForm(forms.ModelForm):
    class Meta:
        model = ReadingStatus 
        fields = ['status', 'progress']  # Campos do modelo ReadingStatus que serão incluídos no formulário

# Formulário para o modelo User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Campo de senha, usando widget PasswordInput para ocultar a entrada

    class Meta:
        model = User  
        fields = ['username', 'email', 'password']  # Campos do modelo User que serão incluídos no formulário

# Formulário para login de usuário
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150) 
    password = forms.CharField(widget=forms.PasswordInput)  # Campo de senha, usando widget PasswordInput para ocultar a entrada
