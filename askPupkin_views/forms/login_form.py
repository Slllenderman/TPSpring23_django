from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        widget=forms.TextInput( 
            attrs = {
                'class': 'form-control fs-5',
                'style': 'max-width: 35rem',
                'placeholder': 'Введите имя пользователя'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput( 
            attrs = {
                'class': 'form-control fs-5',
                'style': 'max-width: 35rem',
                'placeholder': 'Введите пароль'
            }
        )
    )

    def check_auth(self, request):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return True
            else:
                self.fields['password'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                self.fields['username'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                self.add_error("password", ValidationError("Ошибка авторизации"))
                self.add_error("username", ValidationError(""))
                return False