import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Book
from .serializers import BookSerializer
from .repository import BookRepository

@method_decorator(csrf_exempt, name='dispatch')
class BookListView(View):
    def get(self, request):
        books = BookRepository.get_all_books()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = BookRepository.create_book(serializer.validated_data)
            return JsonResponse(BookSerializer(book).data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class BookDetailView(View):
    def get(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        if book is None:
            return JsonResponse({'error': 'Book not found'}, status=404)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        if book is None:
            return JsonResponse({'error': 'Book not found'}, status=404)
        data = json.loads(request.body)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            book = BookRepository.update_book(book, serializer.validated_data)
            return JsonResponse(BookSerializer(book).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        if book is None:
            return JsonResponse({'error': 'Book not found'}, status=404)
        BookRepository.delete_book(book)
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)