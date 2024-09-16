import requests

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views import View
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import View
from .forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    template_name = 'accounts/register.html'

class GoogleAuthCompleteView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        error = request.GET.get('error')

        if error:
            return self.render_error(error)

        if code:
            access_token = self.get_access_token(code)
            if access_token:
                userinfo = self.get_user_info(access_token)
                if userinfo:
                    user = self.get_or_create_user(userinfo)
                    login(request, user)
                    return redirect(reverse('home'))

        return self.render_error('Invalid token or code.')

    def get_access_token(self, code):
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': 'http://localhost/google-auth-complete/',
            'grant_type': 'authorization_code',
        }
        token_response = requests.post(token_url, data=token_data)
        token_json = token_response.json()
        return token_json.get('access_token')

    def get_user_info(self, access_token):
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        userinfo_response = requests.get(userinfo_url, headers={'Authorization': f'Bearer {access_token}'})
        if userinfo_response.status_code == 200:
            return userinfo_response.json()
        return None

    def get_or_create_user(self, userinfo):
        email = userinfo['email']
        first_name = userinfo.get('given_name', '')
        last_name = userinfo.get('family_name', '')
        # Створити або отримати користувача Django
        user, created = User.objects.get_or_create(username=email, defaults={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        })
        return user

    def render_error(self, error_message):
        return render(self.request, 'error.html', {'error': error_message})
