from django import forms
from .models.modelBook import Book
from .models.modelReview import Review
from .models.modelWishList import Wishlist
from django.contrib.auth.models import User
from .models.modelReadingStatus import ReadingStatus

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment'] 


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'author', 'genre', 'description', 'priority']

class ReadingStatusForm(forms.ModelForm):
    class Meta:
        model = ReadingStatus
        fields = ['status', 'progress'] 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

