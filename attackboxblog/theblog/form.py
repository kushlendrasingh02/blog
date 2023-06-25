from django import forms
from .models import Post, Category, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'author', 'category', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', id: 'elder', 'value': '', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Snippet'}), 
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': SummernoteWidget(),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Blog Snippet'}),
        }
        
class CategroyForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Category'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'}),
        }