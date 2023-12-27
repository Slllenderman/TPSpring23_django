from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import login
from askPupkin_models.models import Profile


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput( 
            attrs = {
                'class': 'form-control fs-5',
                'style': 'max-width: 35rem',
                'placeholder': 'Введите имя пользователя'
            }
        )
    )
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
    password1 = forms.CharField(
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
    password2 = forms.CharField(
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput( 
            attrs = {
                'class': 'form-control fs-5',
                'style': 'max-width: 35rem',
                'placeholder': 'Введите пароль'
            }
        )
    )
    avatar = forms.ImageField(
        label='Выберите аватар',
        required=False,
        widget=forms.FileInput(
            attrs = {
                'class':'form-control',
                'style':'max-width: 25rem'
            }
        )
    )

    def check_creation(self, request):
        if self.is_valid():
            email = self.cleaned_data["email"]
            username = self.cleaned_data["username"]
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            avatar = self.cleaned_data["avatar"]
            if password1 != password2:
                self.add_error("password1", ValidationError(""))
                self.add_error("password2", ValidationError("Введённые пароли не совпадают"))
                self.fields['password1'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                self.fields['password2'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                return False
            try:
                User.objects.get(username=username)
                self.add_error("username", ValidationError("Пользователь с таким именим уже существует"))
                self.fields['username'].widget.attrs.update({'class' : 'form-control fs-5 is-invalid'})
                return False
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password1, email=email)
                Profile.objects.create(user=user, avatar=avatar)
                login(request, user)
                return True