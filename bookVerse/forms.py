from django import forms
from .models.modelBook import Book
from .models.modelReview import Review
from .models.modelWishList import Wishlist
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
        fields = ['book', 'priority']

class ReadingStatusForm(forms.ModelForm):
    class Meta:
        model = ReadingStatus
        fields = ['status', 'progress'] 
