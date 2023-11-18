from django.urls import reverse_lazy
from django.contrib.auth import views

from accounts.forms import LoginForm


class LoginView(views.TemplateView):
    template_name = 'registration/login.html'
    form_class = LoginForm



class LogoutView(views.LogoutView):
    pass
