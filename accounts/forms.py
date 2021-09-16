from django import forms
from . import models
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    captcha = CaptchaField(label="captcha")
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserForm(forms.ModelForm):
    captcha = CaptchaField(label='captcha')
    password2 = forms.CharField(label="repeat password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.User
        fields = ['name', 'password', 'email', 'sex']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['sex'].label = 'gender'
        self.fields['email'].label = 'E-mail'
        self.fields['name'].label = 'username'
        self.fields['password'].label = 'password'
