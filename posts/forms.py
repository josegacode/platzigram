from django import forms

from posts.models import Post 

# This is a way to created forms from 
# custom models, using ModelForm provided by
# Django
class PostForm(forms.ModelForm):

    class Meta:
        # Custom model used to create this form 
        model = Post
        
        # Specifies the fields that we will need
        fields = ('user', 'profile', 'title', 'photo')
