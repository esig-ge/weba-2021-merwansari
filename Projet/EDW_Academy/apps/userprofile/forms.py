from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


YEARS = [x for x in range(1940, 2010)]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'birth_date']
        lables = {'username':"Username",'first_name': "First Name", 'last_name': "Last Name", 'email': "Email", 'birth_date': "Birth Date"}

        widgets = {'birth_date': forms.SelectDateWidget(years=YEARS)}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

