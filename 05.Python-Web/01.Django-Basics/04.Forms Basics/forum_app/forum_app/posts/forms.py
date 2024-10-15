from django import forms

from forum_app.posts.choices import LanguageChoices
from forum_app.posts.models import Post


# class PostForm(forms.Form):
#     TITLE_MAX_LENGTH = 100
#     AUTHORS_MAX_LENGTH = 30
#     LANGUAGE_MAX_LENGTH = 20
#
#     title = forms.CharField(max_length=TITLE_MAX_LENGTH, )
#     content = forms.CharField(widget=forms.Textarea, )
#     author = forms.CharField(max_length=AUTHORS_MAX_LENGTH, )
#     created_at = forms.DateTimeField()
#     language = forms.ChoiceField(choices=LanguageChoices.choices, )
#

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        labels = {'title': 'Post\'s title', }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your post title', }, ),
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search post', }, ),
    )