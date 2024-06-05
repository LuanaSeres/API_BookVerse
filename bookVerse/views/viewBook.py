from django.shortcuts import render, get_object_or_404, redirect
from ..forms import BookForm, ReviewForm
from ..models.modelBook import Book
from django.views import View
from ..repository import BookRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class BookListView(View):
    def get(self, request):
        books = BookRepository.get_all_books()
        return render(request, 'book_list.html', {'books': books})
    
@method_decorator(login_required, name='dispatch')
class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book-detail', pk=book.pk)
        return render(request, 'book_form.html', {'form': form})

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = book.reviews.all()
        return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

@method_decorator(login_required, name='dispatch')
class BookUpdateView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'book_form.html', {'form': form})

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
        return render(request, 'book_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class BookDeleteView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'book_confirm_delete.html', {'book': book})

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('book-list')