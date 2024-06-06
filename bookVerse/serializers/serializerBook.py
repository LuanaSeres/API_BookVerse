from rest_framework import serializers
from ..models.modelBook import Book

# Serializer para o modelo Book incluindo todos os campos do mesmo.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  
        fields = '__all__'  
