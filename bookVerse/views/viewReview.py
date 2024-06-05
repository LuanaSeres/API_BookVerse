from django.views import View
from django.shortcuts import render, redirect
from ..forms import ReviewForm
from ..repository import ReviewRepository

class ReviewListView(View):
    def get(self, request):
        reviews = ReviewRepository.get_all_reviews()
        return render(request, 'review_list.html', {'reviews': reviews})

class ReviewDetailView(View):
    def get(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        return render(request, 'review_detail.html', {'review': review})

class ReviewCreateView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'review_form.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = ReviewRepository.create_review(form.cleaned_data)
            return redirect('review-detail', pk=review.id)
        return render(request, 'review_form.html', {'form': form})

class ReviewUpdateView(View):
    def get(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        form = ReviewForm(instance=review)
        return render(request, 'review_form.html', {'form': form, 'review': review})

    def post(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            ReviewRepository.update_review(review, form.cleaned_data)
            return redirect('review-detail', pk=review.id)
        return render(request, 'review_form.html', {'form': form, 'review': review})

class ReviewDeleteView(View):
    def get(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        return render(request, 'review_confirm_delete.html', {'review': review})

    def post(self, request, pk):
        review = ReviewRepository.get_review_by_id(pk)
        ReviewRepository.delete_review(review)
        return redirect('review-list')