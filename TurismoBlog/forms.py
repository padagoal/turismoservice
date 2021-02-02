from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                             label='Titulo del Post')
    photo = forms.ImageField(error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    descripcion_post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 label='Descripcion del Post')

    class Meta:
        model = Post
        fields = ('title_post','photo','descripcion_post',)


class LikePostForm(forms.ModelForm):
    class Meta:
        model = LikesPerUser
        fields = '__all__'
