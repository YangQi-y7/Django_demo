from . import models
from django import forms
from captcha.fields import CaptchaField


class VideoForm(forms.ModelForm):
    captcha = CaptchaField(label='captcha')

    class Meta:
        model = models.Video
        fields = ['title', 'description', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ArticleForm(forms.ModelForm):
    captcha = CaptchaField(label='captcha')

    class Meta:
        model = models.Article
        fields = ['title', 'description', 'part_1', 'part_2', 'part_3']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'part_1': forms.Textarea(attrs={'class': 'form-control'}),
            'part_2': forms.Textarea(attrs={'class': 'form-control'}),
            'part_3': forms.Textarea(attrs={'class': 'form-control'}),
        }
