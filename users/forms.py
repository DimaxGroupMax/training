from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'autocomplete': 'current-password',
                                          'placeholder': 'Введите ваш пароль'}),
    )
    class Meta:
        model=User
        fields = ['username','password']

class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию',
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш E-mail *youremail@example.com',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш пароль',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите ваш пароль',
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = 'Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'autocomplete': 'current-password',
                                          'placeholder': 'Введите ваш пароль'}),
    )
    class Meta:
        model=User
        fields = ['username','password']

class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
        )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'first_name',
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'last_name',
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username',
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
            }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control mt-3',
                'required': False,
            }
        )
    )



