from django.shortcuts import redirect

class LoginRequiredMiddleware:
# Este método é executado uma vez no início e armazena a view que será chamado depois
    def __init__(self, get_response):
        self.get_response = get_response

 # Este método é executado em cada solicitação
    def __call__(self, request):
        # Verifica se o usuário não está autenticado e se a rota não é '/login/'
        if not request.user.is_authenticated and request.path != '/login/':
            # Redireciona para a página de login se o usuário não estiver autenticado
            return redirect('login')
        
        # Caso contrário, continua para o próxima view
        response = self.get_response(request)
        return response
