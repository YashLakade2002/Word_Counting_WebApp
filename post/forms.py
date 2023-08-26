from django import forms
from .models import PostModel


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}))    
    class Meta:
        model = PostModel
        fields = ('title', 'content')


