import os

import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions
def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ""

    if search_name is None:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    elif search_email is None:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    else:
        authors = Author.objects.filter(
            full_name__icontains=search_name, email__icontains=search_email
        ).order_by('-full_name')

    if not authors.exists():
        return ""

    return '\n'.join(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}"
                     for a in authors)


def get_top_publisher() -> str:
    articles = Article.objects.all()
    if not articles.exists():
        return ""

    author = Author.objects.get_authors_by_article_count().first()
    if not author:
        return ""

    return f"Top Author: {author.full_name} with {author.articles_count} published articles."


def get_top_reviewer() -> str:
    reviews = Review.objects.all()
    if not reviews.exists():
        return ""

    author = Author.objects.annotate(reviews_count=Count('reviews')).order_by('-reviews_count', 'email').first()
    if not author:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.reviews_count} published reviews."


def get_latest_article() -> str:
    article = Article.objects.prefetch_related('authors', 'reviews') \
        .annotate(reviews_count=Count('reviews'), avg_rating=Avg('reviews__rating')) \
        .order_by('-published_on').first()

    if not article:
        return ""

    authors = ', '.join(a.full_name for a in article.authors.order_by('full_name'))
    avg_rating = article.avg_rating if article.avg_rating else 0

    return (f"The latest article is: {article.title}. Authors: {authors}."
            f" Reviewed: {article.reviews_count} times. Average Rating: {avg_rating:.2f}.")


def get_top_rated_article() -> str:
    article = Article.objects.prefetch_related('reviews') \
        .annotate(avg_rating=Avg('reviews__rating'), reviews_num=Count('reviews')) \
        .order_by('-avg_rating', 'title').first()

    if not article or article.reviews_num == 0:
        return ""

    return f"The top-rated article is: {article.title}, " \
           f"with an average rating of {article.avg_rating:.2f}, reviewed {article.reviews_num} times."


def ban_author(email=None) -> str:
    if email is None:
        return "No authors banned."

    author = Author.objects.annotate(num_of_reviews=Count('reviews')) \
        .filter(email__exact=email).first()

    if not author:
        return "No authors banned."

    author.is_banned = True
    author.save()

    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {author.num_of_reviews} reviews deleted."
