from django.shortcuts import render, get_object_or_404, redirect
from ..forms import BookForm
from ..models.modelBook import Book
from ..models.modelReadingStatus import ReadingStatus
from django.views import View
from ..repository import BookRepository
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Aplica o decorador login_required ao método dispatch para exigir login em todas as requisições
@method_decorator(login_required, name='dispatch')
class BookListView(View):
    # Método GET para exibir a lista de livros
    def get(self, request):
        books = BookRepository.get_all_books()
        return render(request, 'book_list.html', {'books': books})
    
# Aplica o decorador login_required ao método dispatch para exigir login em todas as requisições
@method_decorator(login_required, name='dispatch')
class BookCreateView(View):
    # Método GET para exibir o formulário de criação de livro
    def get(self, request):
        form = BookForm()
        return render(request, 'book_create.html', {'form': form})

    # Método POST para processar o formulário de criação de livro
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book-detail', pk=book.pk)
        return render(request, 'book_create.html', {'form': form})  # Se o formulário não for válido, renderiza novamente a template com o formulário

# Aplica o decorador login_required ao método dispatch para exigir login em todas as requisições
@method_decorator(login_required, name='dispatch')
class BookDetailView(View):
    # Método GET para exibir os detalhes do livro
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Obtém o livro pelo ID ou retorna um erro 404 se não for encontrado
        reviews = book.reviews.all()
        reading_status = None
        if request.user.is_authenticated:
            reading_status = ReadingStatus.objects.filter(user=request.user, book=book).first()  # Obtém o status de leitura do usuário para o livro, se existir
        return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'reading_status': reading_status})

# Aplica o decorador login_required ao método dispatch para exigir login em todas as requisições
@method_decorator(login_required, name='dispatch')
class BookUpdateView(View):
    # Método GET para exibir o formulário de atualização de livro
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'book_update.html', {'form': form})

    # Método POST para processar o formulário de atualização de livro
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=pk)
        return render(request, 'book_update.html', {'form': form})  # Se o formulário não for válido, renderiza novamente a template com o formulário

# Aplica o decorador login_required ao método dispatch para exigir login em todas as requisições
@method_decorator(login_required, name='dispatch')
class BookDeleteView(View):
    # Método POST para processar a exclusão de um livro
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('book-list')
