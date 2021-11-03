from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []


    def add_pokemon(self, pokemon: Pokemon):
        if any([x for x in self.pokemons if x.name == pokemon.name]):
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        for pok in self.pokemons:
            if pokemon_name == pok.name:
                self.pokemons.remove(pok)
                return f'You have released {pokemon_name}'
        return f"Pokemon is not caught"


    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}' + '\n' + f'Pokemon count {len(self.pokemons)}'
        for poken in self.pokemons:
            result += '\n'
            result += f'- {poken.pokemon_details()}'

        return result







