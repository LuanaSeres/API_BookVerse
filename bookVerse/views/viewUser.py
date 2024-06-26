from django.views import View
from ..forms import UserForm
from ..repository import UserRepository
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Define uma view baseada em classe para gerar (criar) um novo usuário
class UserGenerate(View):
    # Método GET para exibir o formulário de criação de usuário
    def get(self, request):
        form = UserForm()
        return render(request, "user_generate.html", {'form': form})

    # Método POST para processar o formulário de criação de usuário
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            repository = UserRepository()
            user_data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']
            }
            repository.create(user_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # Autentica o usuário recém-criado
            if user is not None:
                login(request, user)  # Faz login do usuário
            return redirect('book-list')
        return render(request, "user_generate.html", {'form': form})  # Se o formulário não for válido, renderiza novamente a template com o formulário


class UserList(View):
    @method_decorator(login_required)
    def get(self, request):
        repository = UserRepository()
        users = repository.get_all()
        return render(request, "user_list.html", {'users': users})

class UserEdit(View):
    @method_decorator(login_required)
    def get(self, request, id):
        repository = UserRepository()
        user = repository.get_by_id(id)
        user_form = UserForm(initial={'username': user.username, 'email': user.email})
        return render(request, "user_edit.html", {"form": user_form, "id": id})

    @method_decorator(login_required)
    def post(self, request, id):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_data = {
                'username': user_form.cleaned_data['username'],
                'email': user_form.cleaned_data['email'],
                'password': user_form.cleaned_data['password']
            }
            repository = UserRepository()
            repository.update(user_data, id)
            return redirect('user_list')
        return render(request, "user_edit.html", {"form": user_form, "id": id})

# Define uma view baseada em classe para login de usuário
class LoginView(View):
    # Método GET para exibir o formulário de login
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'base.html', {'form': form})

    # Método POST para processar o formulário de login
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Autentica o usuário
            if user is not None:
                login(request, user)
                return redirect('book-list')
        return render(request, 'base.html', {'form': form, 'error': 'Invalid username or password'})

    # Define uma view para logout de usuário
    def logout_view(request):
        logout(request)  # Faz logout do usuário
        return redirect('login')
