from rest_framework import serializers
from ..models.modelReview import Review

# Serializer para o modelo Review incluindo todos os campos do mesmo.
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
