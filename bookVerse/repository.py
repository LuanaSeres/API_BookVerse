from .models.modelBook import Book
from .models.modelReview import Review
from .models.modelWishList import Wishlist
from .models.modelReadingStatus import ReadingStatus
from django.contrib.auth.models import User

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


class WishlistRepository:
    @staticmethod
    def get_all_wishlist():
        return Wishlist.objects.all()

    @staticmethod
    def get_wishlist_by_user(user_id):
        return Wishlist.objects.filter(user_id=user_id)

    @staticmethod
    def create_wishlist_item(data):
        user = data.pop('user')
        wishlist_item = Wishlist.objects.create(user=user, **data)
        return wishlist_item

    @staticmethod
    def get_wishlist_item_by_id(item_id):
        return Wishlist.objects.get(id=item_id)

    @staticmethod
    def update_wishlist_item(item_id, data):
        wishlist_item = Wishlist.objects.get(id=item_id)
        for attr, value in data.items():
            setattr(wishlist_item, attr, value)
        wishlist_item.save()
        return wishlist_item


    @staticmethod
    def delete_wishlist_item(item_id):
        wishlist_item = Wishlist.objects.get(id=item_id)
        wishlist_item.delete()


class ReadingStatusRepository:
    def get_reading_status_by_user_and_book(user_id, book_id):
        try:
            return ReadingStatus.objects.get(user_id=user_id, book_id=book_id)
        except ReadingStatus.DoesNotExist:
            return None

    def create_reading_status(data):
        reading_status = ReadingStatus.objects.create(**data)
        return reading_status

    def update_reading_status(reading_status, data):
        for field, value in data.items():
            setattr(reading_status, field, value)
        reading_status.save()
        return 

    def delete_reading_status(reading_status):
        reading_status.delete()


class UserRepository:
    def get_all(self):
        return User.objects.all()

    def get_by_id(self, id):
        return User.objects.get(id=id)

    def create(self, user_data):
        user = User.objects.create_user(**user_data)
        return user

    def update(self, user_data, id):
        user = User.objects.get(id=id)
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        if user_data.get('password'):
            user.set_password(user_data['password'])
        user.save()
        return user

    def delete(self, id):
        User.objects.get(id=id).delete()