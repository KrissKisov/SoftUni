from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    valid_musician_types = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        try:
            musician = self.valid_musician_types[musician_type](name, age)
        except KeyError:
            raise ValueError("Invalid musician type!")

        musician_exists = next((m for m in self.musicians if m.name == name), None)
        if musician_exists:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        band_exists = next((b for b in self.bands if b.name == name), None)
        if band_exists:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        concert_exists = next((c for c in self.concerts if c.place == place), None)
        if concert_exists:
            raise Exception(f"{place} is already registered for {concert_exists.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        band = next((b for b in self.bands if b.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next((m for m in band.members if m.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        band = next(b for b in self.bands if b.name == band_name)
        singers_count = 0
        drummers_count = 0
        guitarists_count = 0

        for member in band.members:
            if member.__class__.__name__ == "Singer":
                singers_count += 1
            elif member.__class__.__name__ == "Drummer":
                drummers_count += 1
            elif member.__class__.__name__ == "Guitarist":
                guitarists_count += 1

        if not singers_count or not drummers_count or not guitarists_count:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(c for c in self.concerts if c.place == concert_place)
        missing_skill = False

        if concert.genre == "Rock":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Guitarist":
                    if "play rock" not in musician.skills:
                        missing_skill = True
                        break

        elif concert.genre == "Metal":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drumsticks" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Singer":
                    if "sing low pitch notes" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Guitarist":
                    if "play metal" not in musician.skills:
                        missing_skill = True
                        break

        elif concert.genre == "Jazz":
            for musician in band.members:
                if musician.__class__.__name__ == "Drummer":
                    if "play the drums with drum brushes" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Singer":
                    if "sing high pitch notes" not in musician.skills or "sing low pitch notes" not in musician.skills:
                        missing_skill = True
                        break
                elif musician.__class__.__name__ == "Guitarist":
                    if "play jazz" not in musician.skills:
                        missing_skill = True
                        break

        if missing_skill:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit :.2f}$ from the {concert.genre} concert in {concert_place}."
