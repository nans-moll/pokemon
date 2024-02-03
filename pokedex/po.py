import json

class Pokedex:
    def __init__(self):
        self.pokedata = {}

    def load_from_json(self, file_path):
        with open(file_path, 'r') as file:
            self.pokedata = json.load(file)

    def get_pokemon_info(self, pokemon_name):
        return self.pokedata.get(pokemon_name)

# Exemple d'utilisation
pokedex = Pokedex()
pokedex.load_from_json('pokedata.json')  # Assurez-vous d'avoir un fichier 'pokedata.json' avec les informations des Pokémon
pokemon_info = pokedex.get_pokemon_info('Pikachu')
if pokemon_info:
    print(pokemon_info)
else:
    print("Ce Pokémon n'est pas répertorié dans le Pokedex.")
