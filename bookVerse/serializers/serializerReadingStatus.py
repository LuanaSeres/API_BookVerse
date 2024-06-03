from rest_framework import serializers
from ..models.modelReadingStatus import ReadingStatus

class ReadingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingStatus
        fields = '_all_'