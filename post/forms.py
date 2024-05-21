from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'is_draft')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_draft'].label = 'Save as draft'
