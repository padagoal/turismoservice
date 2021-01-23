from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                             label='Titulo del Post')
    photo = forms.ImageField()

    descripcion_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 label='Descripcion del Post')

    class Meta:
        model = Post
        fields = ('title_post','photo','descripcion_post',)