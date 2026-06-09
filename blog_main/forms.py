from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
  pass