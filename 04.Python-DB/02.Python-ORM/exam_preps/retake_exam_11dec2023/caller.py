import os
import django
from django.db.models import Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions
def get_tennis_players(search_name=None, search_country=None) -> str:
    if search_name is None and search_country is None:
        return ""

    tennis_players = None

    if search_name is not None and search_country is not None:
        tennis_players = TennisPlayer.objects.filter(
            full_name__icontains=search_name, country__icontains=search_country
        )

    elif search_name is not None:
        tennis_players = TennisPlayer.objects.filter(full_name__icontains=search_name)

    elif search_country is not None:
        tennis_players = TennisPlayer.objects.filter(country__icontains=search_country)

    if not tennis_players.exists():
        return ""

    return '\n'.join(f"Tennis Player: {t.full_name}, country: {t.country}, ranking: {t.ranking}"
                     for t in tennis_players.order_by('ranking'))


def get_top_tennis_player() -> str:
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not top_player:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.num_wins} wins."


def get_tennis_player_by_matches_count() -> str:
    matches = Match.objects.all()
    if not matches.exists():
        return ""

    player = TennisPlayer.objects.annotate(matches_count=Count('matches')) \
        .order_by('-matches_count', 'ranking').first()

    if not player:
        return ""

    return f"Tennis Player: {player.full_name} with {player.matches_count} matches played."


def get_tournaments_by_surface_type(surface=None) -> str:
    if surface is None:
        return ""

    tournaments = Tournament.objects.filter(surface_type__icontains=surface) \
        .annotate(num_matches=Count('matches')).order_by('-start_date')

    if not tournaments.exists():
        return ""

    return '\n'.join(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}"
                     for t in tournaments)


def get_latest_match_info() -> str:
    match = Match.objects.prefetch_related('players') \
        .select_related('tournament').order_by('-date_played', '-id').first()

    if not match:
        return ""

    players = match.players.order_by('full_name')
    winner = "TBA" if match.winner is None else match.winner.full_name

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, score: {match.score}, "
            f"players: {players[0].full_name} vs {players[1].full_name},"
            f" winner: {winner}, summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None) -> str:
    pass
    if tournament_name is None:
        return "No matches found."

    tournament = Tournament.objects.filter(name__exact=tournament_name).first()

    if not tournament:
        return "No matches found."

    matches = Match.objects.select_related('tournament') \
        .filter(tournament=tournament).order_by('-date_played')

    if not matches.exists():
        return "No matches found."

    return '\n'.join(f"Match played on: {m.date_played}, score: {m.score}, "
                     f"winner: {'TBA' if m.winner is None else m.winner.full_name}"
                     for m in matches)
