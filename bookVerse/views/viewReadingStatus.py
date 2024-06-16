from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..models.modelReadingStatus import ReadingStatus
from ..models.modelBook import Book
from ..forms import ReadingStatusForm
from ..repository import ReadingStatusRepository

# Define uma view baseada em classe para listar todos os status de leitura
class ReadingStatusListView(View):
    # Método GET para exibir a lista de status de leitura
    def get(self, request):
        reading_statuses = ReadingStatusRepository.get_all_reading_statuses() 
        return render(request, 'reading_status_list.html', {'reading_statuses': reading_statuses})

# Define uma view baseada em classe para exibir os detalhes de um status de leitura
class ReadingStatusDetailView(View):
    # Método GET para exibir os detalhes do status de leitura
    def get(self, request, pk):
        reading_status = ReadingStatusRepository.get_reading_status_by_id(pk)
        return render(request, 'reading_status_detail.html', {'reading_status': reading_status})
    
# Define uma view baseada em classe para criar um novo status de leitura
class ReadingStatusCreateView(View):
    # Método GET para exibir o formulário de criação de status de leitura
    def get(self, request):
        form = ReadingStatusForm()
        return render(request, 'reading_status_form.html', {'form': form})
    
    # Método POST para processar o formulário de criação de status de leitura
    def post(self, request):
        form = ReadingStatusForm(request.POST)
        if form.is_valid():
            reading_status = ReadingStatusRepository.create_reading_status(form.cleaned_data)
            return redirect('reading-status-detail', pk=reading_status.id) 
        return render(request, 'reading_status_form.html', {'form': form}) 

# Define uma view baseada em classe para atualizar um status de leitura existente, exigindo que o usuário esteja logado
class UpdateReadingStatusView(LoginRequiredMixin, View):
    # Método GET para exibir o formulário de atualização de status de leitura
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        reading_status, _ = ReadingStatus.objects.get_or_create(user=request.user, book=book)  
        form = ReadingStatusForm(instance=reading_status)
        reviews = book.reviews.all()
        return render(request, 'book_detail.html', {
            'book': book,
            'reading_status': reading_status,
            'reviews': reviews,
            'form': form,
        })

    # Método POST para processar o formulário de atualização de status de leitura
    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        reading_status, _ = ReadingStatus.objects.get_or_create(user=request.user, book=book) 
        form = ReadingStatusForm(request.POST, instance=reading_status)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=book_id)
        reviews = book.reviews.all()
        return render(request, 'book_detail.html', {
            'book': book,
            'reading_status': reading_status,
            'reviews': reviews,
            'form': form,
        }) 
