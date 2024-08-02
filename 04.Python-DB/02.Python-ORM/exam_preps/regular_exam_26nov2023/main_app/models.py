from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.custom_managers import AuthorManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
    )
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2005)],
    )
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()


class CommonFields(models.Model):
    content = models.TextField(
        validators=[MinLengthValidator(10)],
    )
    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        abstract = True


class CategoryChoices(models.TextChoices):
    TECHNOLOGY = "Technology", "Technology"
    SCIENCE = "Science", "Science"
    EDUCATION = "Education", "Education"


class Article(CommonFields):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
    )
    category = models.CharField(
        choices=CategoryChoices.choices,
        max_length=10,
        default=CategoryChoices.TECHNOLOGY,
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name='articles',
    )


class Review(CommonFields):
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
