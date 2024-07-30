import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie

from django.db.models import Count, Avg, F


# Create queries within functions
def get_directors(search_name=None, search_nationality=None) -> str:

    if search_name is None and search_nationality is None:
        return ""

    if search_name is None:
        directors = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')

    elif search_nationality is None:
        directors = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')

    else:
        directors = Director.objects.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality,
        ).order_by('full_name')

    if not directors:
        return ""

    return '\n'.join(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
                     for d in directors)


def get_top_director() -> str:
    director = Director.objects.get_directors_by_movies_count().first()

    if not director:
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor() -> str:
    actor = Actor.objects.prefetch_related('starring_actor_movies').annotate(
        count_of_movie=Count('starring_actor_movies'),
        avg_rating=Avg('starring_actor_movies__rating'),
    ).order_by('-count_of_movie', 'full_name').first()

    if not actor or not actor.count_of_movie:
        return ""

    movies = ', '.join(m.title for m in actor.starring_actor_movies.all())

    return (f"Top Actor: {actor.full_name}, starring in movies: {movies}, "
            f"movies average rating: {actor.avg_rating:.1f}")


def get_actors_by_movies_count() -> str:
    actors = Actor.objects.annotate(
        count_of_movies=Count('actor_movies')
    ).order_by('-count_of_movies', 'full_name')[:3]

    if not actors or not actors[0].count_of_movies:
        return ""

    return '\n'.join(f"{a.full_name}, participated in {a.count_of_movies} movies" for a in actors)


def get_top_rated_awarded_movie() -> str:
    movie = Movie.objects.filter(is_awarded=True)\
        .select_related('starring_actor').prefetch_related('actors')\
        .order_by('-rating', 'title') .first()

    if not movie:
        return ""

    main_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    cast = ', '.join(movie.actors.all().order_by('full_name').values_list('full_name', flat=True))

    return (f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}."
            f" Starring actor: {main_actor}. Cast: {cast}.")


def increase_rating() -> str:
    movies = Movie.objects.filter(is_classic=True, rating__lte=9.9)

    if not movies:
        return "No ratings increased."

    movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {movies.count()} movies."
