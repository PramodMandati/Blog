from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View, CreateView

from .forms import UserCreationForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('post:home_page')

    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return redirect(reverse('post:home_page'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('account:login_page'))


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login_page')


class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account:login_page')
    template_name = 'home_page.html'
