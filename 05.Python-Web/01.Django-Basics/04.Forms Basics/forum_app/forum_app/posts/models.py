from django.db import models

from forum_app.posts.choices import LanguageChoices


class Post(models.Model):
    TITLE_MAX_LENGTH = 100
    AUTHORS_MAX_LENGTH = 30
    LANGUAGE_MAX_LENGTH = 20

    title = models.CharField(max_length=TITLE_MAX_LENGTH, )
    content = models.TextField()
    author = models.CharField(max_length=AUTHORS_MAX_LENGTH, )
    created_at = models.DateTimeField(auto_now_add=True, )
    languages = models.CharField(
        max_length=LANGUAGE_MAX_LENGTH,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )
