import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models.modelReadingStatus import ReadingStatus
from ..serializers.serializerReadingStatus import ReadingStatusSerializer
from ..repository import ReadingStatusRepository

@method_decorator(csrf_exempt, name='dispatch')
class ReadingStatusView(View):
    def get(self, request):
        reading_statuses = ReadingStatusRepository.get_all_reading_status()
        serializer = ReadingStatusSerializer(reading_statuses, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = ReadingStatusSerializer(data=data)
        if serializer.is_valid():
            reading_status = ReadingStatusRepository.create_reading_status(serializer.validated_data)
            return JsonResponse(ReadingStatusSerializer(reading_status).data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ReadingStatusDetailView(View):
    def get(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        if reading_status is None:
            return JsonResponse({'error': 'Reading status not found'}, status=404)
        serializer = ReadingStatusSerializer(reading_status)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        if reading_status is None:
            return JsonResponse({'error': 'Reading status not found'}, status=404)
        data = json.loads(request.body)
        serializer = ReadingStatusSerializer(reading_status, data=data)
        if serializer.is_valid():
            reading_status = ReadingStatusRepository.update_reading_status(reading_status, serializer.validated_data)
            return JsonResponse(ReadingStatusSerializer(reading_status).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        if reading_status is None:
            return JsonResponse({'error': 'Reading status not found'}, status=404)
        ReadingStatusRepository.delete_reading_status(reading_status)
        return JsonResponse({'message': 'Reading status deleted successfully'}, status=204)