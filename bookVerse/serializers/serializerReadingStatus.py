from rest_framework import serializers
from ..models.modelReadingStatus import ReadingStatus

# Serializer para o modelo ReadingStatus incluindo todos os campos do mesmo.
class ReadingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingStatus  
        fields = '__all__'  
