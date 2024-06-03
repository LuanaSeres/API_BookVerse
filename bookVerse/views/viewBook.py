from django.shortcuts import render, redirect
from .forms import BookForm
from django.views import View
from ..repository import BookRepository

class BookListView(View):
    def get(self, request):
        books = BookRepository.get_all_books()
        return render(request, 'books/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        return render(request, 'books/book_detail.html', {'book': book})

class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'books/book_form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = BookRepository.create_book(form.cleaned_data)
            return redirect('book-detail', pk=book.id)
        return render(request, 'books/book_form.html', {'form': form})

class BookUpdateView(View):
    def get(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        form = BookForm(instance=book)
        return render(request, 'books/book_form.html', {'form': form, 'book': book})

    def post(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            BookRepository.update_book(book, form.cleaned_data)
            return redirect('book-detail', pk=book.id)
        return render(request, 'books/book_form.html', {'form': form, 'book': book})

class BookDeleteView(View):
    def get(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        return render(request, 'books/book_confirm_delete.html', {'book': book})

    def post(self, request, pk):
        book = BookRepository.get_book_by_id(pk)
        BookRepository.delete_book(book)
        return redirect('book-list')