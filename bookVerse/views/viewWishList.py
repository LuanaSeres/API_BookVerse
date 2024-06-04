from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from ..models.modelWishList import Wishlist
from ..forms import WishlistForm
from ..repository import WishlistRepository


class WishListView(View):
    def get(self, request):
        wishlist = WishlistRepository.get_all_wishlist_items()
        return render(request, 'wishlist_list.html', {'wishlist': wishlist})

class WishlistDetailView(View):
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        return render(request, 'wishlist_detail.html', {'wishlist_item': wishlist_item})

class WishlistCreateView(View):
    def get(self, request):
        form = WishlistForm()
        return render(request, 'wishlist_form.html', {'form': form})

    def post(self, request):
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = WishlistRepository.create_wishlist_item(form.cleaned_data)
            return redirect('wishlist-detail', pk=wishlist_item.id)
        return render(request, 'wishlist_form.html', {'form': form})

class WishlistUpdateView(View):
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        form = WishlistForm(instance=wishlist_item)
        return render(request, 'wishlist_form.html', {'form': form, 'wishlist_item': wishlist_item})

    def post(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        form = WishlistForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            WishlistRepository.update_wishlist_item(wishlist_item, form.cleaned_data)
            return redirect('wishlist-detail', pk=wishlist_item.id)
        return render(request, 'wishlist_form.html', {'form': form, 'wishlist_item': wishlist_item})

class WishlistDeleteView(View):
    def get(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        return render(request, 'wishlist_confirm_delete.html', {'wishlist_item': wishlist_item})

    def post(self, request, pk):
        wishlist_item = WishlistRepository.get_wishlist_item_by_id(pk)
        WishlistRepository.delete_wishlist_item(wishlist_item)
        return redirect('wishlist-list')
