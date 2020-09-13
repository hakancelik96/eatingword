from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.utils.deprecation import MiddlewareMixin


class RedirectAnonymousUser(MiddlewareMixin):
    redirect_url = "account:login"
    allow_urls = ("account:login", "account:register")

    def process_request(self, request):
        url_info = resolve(request.path_info)
        if url_info.app_names:
            current_url_name = url_info.app_names[0] + ":" + url_info.url_name
        else:
            current_url_name = url_info.url_name
        if (
            request.user.is_anonymous
            and current_url_name not in self.allow_urls
        ):
            return redirect(reverse(self.redirect_url))
