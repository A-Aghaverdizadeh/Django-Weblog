from .models import Comment, Post
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        labels = {
            'body': '',
        }
        
        widgets = {
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Comment',
                'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Retrieve the user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            # Populate the initial values with user information
            self.initial['name'] = user.username
            self.initial['email'] = user.email


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter search term...', "aria-label": "", "aria-describedby": ""}),
        label=''
    )

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'image', 'status', 'tags']

        labels = {
            'title': '',
            'slug': '',
            'body': '',
            'image': '',
            'status': '',
            'tags': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title', 'style': 'box-shadow: 0 0 10px #f29263'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Slug', 'style': 'box-shadow: 0 0 10px #f29263'}),
            'body': CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Post Body', 'style': 'box-shadow: 0 0 10px #f29263'}),
            'image': forms.FileInput(attrs={'class': 'btn btn-warning', 'placeholder': '', 'style': 'box-shadow: 0 0 10px #f29263'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'box-shadow: 0 0 10px #f29263'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Tags', 'style': 'box-shadow: 0 0 10px #f29263'})
        }
