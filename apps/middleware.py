from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils.deprecation import MiddlewareMixin


class RedirectAnonymousUser(MiddlewareMixin):
    redirect_url = "login"
    allow_urls = ("login", "register")

    def process_request(self, request):
        current_url_name = resolve(request.path_info).url_name
        if (
            request.user.is_anonymous
            and current_url_name not in self.allow_urls
        ):
            return redirect(reverse(self.redirect_url))
