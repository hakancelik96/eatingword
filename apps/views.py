from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class MessageMixin(SuccessMessageMixin):
    success_message = "Successfully Created/Updated"

    def form_invalid(self, form):
        messages.error(self.request, "Form Invalid")
        return super().form_invalid(form)
