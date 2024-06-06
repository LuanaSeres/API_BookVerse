from rest_framework import serializers
from ..models.modelWishList import Wishlist

# Serializer para o modelo Wishlist incluindo todos os campos do mesmo.
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'