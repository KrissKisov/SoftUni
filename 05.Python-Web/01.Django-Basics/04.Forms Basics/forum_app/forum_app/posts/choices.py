from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'py', 'Pythoon'
    JAVASCRIPT = 'js', 'Javascript'
    C = 'c', 'C'
    C_PLUS_PLUS = 'cpp', 'C++'
    OTHER = 'other', 'Other'
