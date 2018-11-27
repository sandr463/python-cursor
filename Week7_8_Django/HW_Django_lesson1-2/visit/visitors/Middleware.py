from django.http import HttpResponseRedirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if not request.user.is_authenticated:
            if not request.path.startswith('/login'):
                return HttpResponseRedirect('login')

        return response
