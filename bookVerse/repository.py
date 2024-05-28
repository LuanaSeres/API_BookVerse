from .models.modelBook import Book

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
