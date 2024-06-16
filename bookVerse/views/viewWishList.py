from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from ..models.modelWishList import Wishlist
from ..forms import WishlistForm
from ..repository import WishlistRepository

# Define uma view baseada em classe para exibir a lista de itens de wishlist
class WishlistListView(View):
    # Método GET para exibir a lista de desejos
    def get(self, request):
        wishlist_items = WishlistRepository.get_wishlist_by_user(request.user.id)
        return render(request, 'wishlist_list.html', {'wishlist_items': wishlist_items})

# Define uma view baseada em classe para exibir detalhes de um item de wishlist
class WishlistDetailView(View):
    # Método GET para exibir os detalhes do livro
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        if not wishlist_item:
            return redirect('wishlist-list')  # Redireciona para a lista de wishlist se o item não for encontrado
        return render(request, 'wishlist_detail.html', {'wishlist_item': wishlist_item})

# Define uma view baseada em classe para criar um novo item de wishlist
class WishlistCreateView(View):
    # Método GET para exibir o formulário de criação do livro na lista de desejos
    def get(self, request):
        form = WishlistForm()
        return render(request, 'wishlist_create.html', {'form': form})

    # Método POST para processar o formulário de criação do livro na lista de desejos
    def post(self, request):
        form = WishlistForm(request.POST)
        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            data['user'] = user
            WishlistRepository.create_wishlist_item(data)
            return redirect('wishlist-list')
        return render(request, 'wishlist_create.html', {'form': form})

# Define uma view baseada em classe para atualizar um item de wishlist existente
class WishlistUpdateView(View):
    # Método GET para exibir o formulário de atualização do livro na lista de desejos
    def get(self, request, pk):
        wishlist_item = get_object_or_404(Wishlist, pk=pk)
        form = WishlistForm(instance=wishlist_item)
        return render(request, 'wishlist_update.html', {'form': form})

    # Método POST para processar o formulário de atualização do livro na lista de desejos
    def post(self, request, pk):
        wishlist_item = get_object_or_404(Wishlist, pk=pk)
        form = WishlistForm(request.POST, instance=wishlist_item)
        if form.is_valid(): 
            updated_data = form.cleaned_data
            WishlistRepository.update_wishlist_item(pk, updated_data)
            return redirect('wishlist-detail', pk=pk)
        return render(request, 'wishlist_update.html', {'form': form})

# Define uma view baseada em classe para deletar um item de wishlist
class WishlistDeleteView(View):
    # Método POST para processar a exclusão de um livro na lista de desejos
    def post(self, request, pk):
        WishlistRepository.delete_wishlist_item(pk)
        return redirect('wishlist-list')
