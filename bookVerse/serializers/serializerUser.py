from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer para o modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ('id', 'username', 'email', 'password')  # Inclui apenas os campos id, username, email e password no serializer
        extra_kwargs = {'password': {'write_only': True}}  # Define que o campo password é apenas para escrita, não será retornado na resposta

    # Método para criar um novo usuário
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Cria um novo usuário usando o método create_user, que lida com a hash da senha
        return user  # Retorna o usuário criado
