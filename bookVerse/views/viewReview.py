from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from ..models.modelReview import Review
from ..models.modelBook import Book
from ..forms import ReviewForm
from ..repository import ReviewRepository

class ReviewCreateView(View):
    def get(self, request, book_pk):
        form = ReviewForm()
        return render(request, 'review_form.html', {'form': form, 'book_pk': book_pk})

    def post(self, request, book_pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = get_object_or_404(Book, pk=book_pk)
            review.user = request.user
            review.save()
            return redirect('book-detail', pk=book_pk)
        return render(request, 'review_form.html', {'form': form, 'book_pk': book_pk})

class ReviewUpdateView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(instance=review)
        return render(request, 'review_form.html', {'form': form, 'book_pk': review.book.pk})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=review.book.pk)
        return render(request, 'review_form.html', {'form': form, 'book_pk': review.book.pk})

class ReviewDeleteView(View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        book_pk = review.book.pk
        review.delete()
        return redirect('book-detail', pk=book_pk)