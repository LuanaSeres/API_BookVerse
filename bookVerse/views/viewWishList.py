import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models.modelWishList import Wishlist
from ..serializers.serializerWishList import WishlistSerializer
from ..repository import WishlistRepository

@method_decorator(csrf_exempt, name='dispatch')
class WishListView(View):
    def post(self, request):
        data = json.loads(request.body)
        serializer = WishlistSerializer(data=data)
        if serializer.is_valid():
            wishlist = WishlistRepository.create_wishlist(serializer.validated_data)
            return JsonResponse(WishlistSerializer(wishlist).data, status=201)
        return JsonResponse(serializer.errors, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class WishlistDetailView(View):
    def get(self, request, user_id):
        wishlist = WishlistRepository.get_wishlist_by_user(user_id)
        if wishlist is None:
            return JsonResponse({'error': 'Wishlist not found'}, status=404)
        serializer = WishlistSerializer(wishlist)
        return JsonResponse(serializer.data)

    def put(self, request, user_id):
        wishlist = WishlistRepository.get_wishlist_by_user(user_id)
        if wishlist is None:
            return JsonResponse({'error': 'Wishlist not found'}, status=404)
        data = json.loads(request.body)
        serializer = WishlistSerializer(wishlist, data=data)
        if serializer.is_valid():
            wishlist = WishlistRepository.update_wishlist(wishlist, serializer.validated_data)
            return JsonResponse(WishlistSerializer(wishlist).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, user_id):
        wishlist = WishlistRepository.get_wishlist_by_user(user_id)
        if wishlist is None:
            return JsonResponse({'error': 'Wishlist not found'}, status=404)
        WishlistRepository.delete_wishlist(wishlist)
        return JsonResponse({'message': 'Wishlist deleted successfully'}, status=204)