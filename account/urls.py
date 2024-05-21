from django.urls import path

from .views import LoginView, UserRegistrationView, HomePageView, LogoutView

app_name = 'account'

urlpatterns = [
    path('login', LoginView.as_view(), name='login_page'),
    path('register', UserRegistrationView.as_view(), name='registration_page'),
    # path('home', HomePageView.as_view(), name='home_page'),
    path('logout', LogoutView.as_view(), name='logout'),
]
