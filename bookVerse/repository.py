from .models.modelBook import Book
from .models.modelReview import Review

class BookRepository:
    def get_all_books():
        return Book.objects.all()

    def get_book_by_id(book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    def create_book(data):
        book = Book.objects.create(**data)
        return book

    def update_book(book, data):
        for field, value in data.items():
            setattr(book, field, value)
        book.save()
        return book

    def delete_book(book):
        book.delete()


class ReviewRepository:
    def get_all_reviews():
        return Review.objects.all()

    def get_review_by_id(review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return None

    def create_review(data):
        review = Review.objects.create(**data)
        return review

    def update_review(review, data):
        for field, value in data.items():
            setattr(review, field, value)
        review.save()
        return review

    def delete_review(review):
        review.delete()
