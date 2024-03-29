from typing import List
from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

        # pokemon = None
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         pokemon = p
        #         self.pokemons.remove(pokemon)
        #         return f"You have released {pokemon_name}"
        #
        # return "Pokemon is not caught"

    def trainer_data(self) -> str:
        pokemons_info = "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n"
                f"{pokemons_info}")
