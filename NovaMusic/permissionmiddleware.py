from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass
        # if not request.user.is_authenticated and request.path not in ('/login/', '/register/'):
        #     return HttpResponseRedirect(reverse('login'))