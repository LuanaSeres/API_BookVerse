import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models.modelReview import Review
from ..serializers.serializerReview import ReviewSerializer
from ..repository import ReviewRepository

@method_decorator(csrf_exempt, name='dispatch')
class ReviewListView(View):
    def get(self, request):
        reviews = ReviewRepository.get_all_reviews()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            review = ReviewRepository.create_review(serializer.validated_data)
            return JsonResponse(ReviewSerializer(review).data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ReviewDetailView(View):
    def get(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        if review is None:
            return JsonResponse({'error': 'Review not found'}, status=404)
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        if review is None:
            return JsonResponse({'error': 'Review not found'}, status=404)
        data = json.loads(request.body)
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            review = ReviewRepository.update_review(review, serializer.validated_data)
            return JsonResponse(ReviewSerializer(review).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        if review is None:
            return JsonResponse({'error': 'Review not found'}, status=404)
        ReviewRepository.delete_review(review)
        return JsonResponse({'message': 'Review deleted successfully'}, status=204)
