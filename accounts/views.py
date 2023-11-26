from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import views, login
from django.views.generic import CreateView
from accounts.forms import LoginForm, RegisterForm
from accounts.models import User


class LoginView(views.LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('home')




class LogoutView(views.LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def form_valid(self, form):

        user = form.save()

        login(self.request, user)

        return reverse('home')
    
    def form_invalid(self, form):
        print(form.errors)
        return redirect('home')
