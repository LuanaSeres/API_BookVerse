from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from ..models.modelWishList import Wishlist
from ..forms import WishlistForm
from ..repository import WishlistRepository
from ..models.modelWishList import Wishlist



class WishlistListView(View):
    def get(self, request):
        wishlist_items = WishlistRepository.get_wishlist_by_user(request.user.id)
        return render(request, 'wishlist_list.html', {'wishlist_items': wishlist_items})





class WishlistDetailView(View):
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        if not wishlist_item:
            return redirect('wishlist-list')  # Redirecionar se o item não for encontrado
        return render(request, 'wishlist_detail.html', {'wishlist_item': wishlist_item})


class WishlistCreateView(View):
    def get(self, request):
        form = WishlistForm()
        return render(request, 'wishlist_form.html', {'form': form})

    def post(self, request):
        form = WishlistForm(request.POST)
        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            data['user'] = user
            WishlistRepository.create_wishlist_item(data)
            return redirect('wishlist-list')
        return render(request, 'wishlist_form.html', {'form': form})



                      
class WishlistUpdateView(View):
    def get(self, request, pk):
        wishlist_item = get_object_or_404(Wishlist, pk=pk)
        form = WishlistForm(instance=wishlist_item)
        return render(request, 'wishlist_form.html', {'form': form})

    def post(self, request, pk):
        wishlist_item = get_object_or_404(Wishlist, pk=pk)
        form = WishlistForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            updated_data = form.cleaned_data
            WishlistRepository.update_wishlist_item(pk, updated_data)
            return redirect('wishlist-detail', pk=pk)
        return render(request, 'wishlist_form.html', {'form': form})


class WishlistDeleteView(View):
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        return render(request, 'wishlist_confirm_delete.html', {'wishlist_item': wishlist_item})

    def post(self, request, pk):
        WishlistRepository.delete_wishlist_item(pk)
        return redirect('wishlist-list')