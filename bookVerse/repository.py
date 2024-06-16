from .models.modelBook import Book
from .models.modelReview import Review
from .models.modelWishList import Wishlist
from .models.modelReadingStatus import ReadingStatus
from django.contrib.auth.models import User 

# Repositório para operações relacionadas ao modelo Book
class BookRepository:
    # Retorna todos os livros
    def get_all_books():
        return Book.objects.all()

    # Retorna um livro pelo seu ID
    def get_book_by_id(book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return None

    # Cria um novo livro com os dados fornecidos
    def create_book(data):
        book = Book.objects.create(**data)
        return book

    # Atualiza um livro existente com novos dados
    def update_book(book, data):
        for field, value in data.items():
            setattr(book, field, value)
        book.save()
        return book

    # Deleta um livro
    def delete_book(book):
        book.delete()


# Repositório para operações relacionadas ao modelo Review
class ReviewRepository:
    # Retorna todas as resenhas
    def get_all_reviews():
        return Review.objects.all()

    # Retorna uma resenha pelo seu ID
    def get_review_by_id(review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return None

    # Cria uma nova resenha com os dados fornecidos
    def create_review(data):
        review = Review.objects.create(**data)
        return review

    # Atualiza uma resenha existente com novos dados
    def update_review(review, data):
        for field, value in data.items():
            setattr(review, field, value)
        review.save()
        return review

    # Deleta uma resenha
    def delete_review(review):
        review.delete()


# Repositório para operações relacionadas ao modelo Wishlist
class WishlistRepository:
    # Retorna todos os itens da lista de desejos
    @staticmethod
    def get_all_wishlist():
        return Wishlist.objects.all()

    # Retorna a lista de desejos de um usuário específico
    @staticmethod
    def get_wishlist_by_user(user_id):
        return Wishlist.objects.filter(user_id=user_id)

    # Cria um novo item na lista de desejos com os dados fornecidos
    @staticmethod
    def create_wishlist_item(data):
        user = data.pop('user')
        wishlist_item = Wishlist.objects.create(user=user, **data)
        return wishlist_item

    # Retorna um item específico da lista de desejos pelo seu ID
    @staticmethod
    def get_wishlist_item_by_id(item_id):
        return Wishlist.objects.get(id=item_id)

    # Atualiza um item da lista de desejos com novos dados
    @staticmethod
    def update_wishlist_item(item_id, data):
        wishlist_item = Wishlist.objects.get(id=item_id)
        for attr, value in data.items():
            setattr(wishlist_item, attr, value)
        wishlist_item.save()
        return wishlist_item

    # Deleta um item da lista de desejos
    @staticmethod
    def delete_wishlist_item(item_id):
        wishlist_item = Wishlist.objects.get(id=item_id)
        wishlist_item.delete()


# Repositório para operações relacionadas ao modelo ReadingStatus
class ReadingStatusRepository:
    # Retorna o status de leitura de um usuário para um livro específico
    def get_reading_status_by_user_and_book(user_id, book_id):
        try:
            return ReadingStatus.objects.get(user_id=user_id, book_id=book_id)
        except ReadingStatus.DoesNotExist:
            return None

    # Cria um novo status de leitura com os dados fornecidos
    def create_reading_status(data):
        reading_status = ReadingStatus.objects.create(**data)
        return reading_status

    # Atualiza um status de leitura existente com novos dados
    def update_reading_status(reading_status, data):
        for field, value in data.items():
            setattr(reading_status, field, value)
        reading_status.save()
        return reading_status

    # Deleta um status de leitura
    def delete_reading_status(reading_status):
        reading_status.delete()


# Repositório para operações relacionadas ao modelo User
class UserRepository:
    # Retorna todos os usuários
    def get_all(self):
        return User.objects.all()

    # Retorna um usuário pelo seu ID
    def get_by_id(self, id):
        return User.objects.get(id=id)

    # Cria um novo usuário com os dados fornecidos
    def create(self, user_data):
        user = User.objects.create_user(**user_data)
        return user

    # Atualiza um usuário existente com novos dados
    def update(self, user_data, id):
        user = User.objects.get(id=id)
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        if user_data.get('password'):
            user.set_password(user_data['password'])
        user.save()
        return user

    # Deleta um usuário
    def delete(self, id):
        User.objects.get(id=id).delete()
