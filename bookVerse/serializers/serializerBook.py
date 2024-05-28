from rest_framework import serializers
from ..models.modelBook import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'