import random
from models import Pokemon

def battle(pokemons) -> str:
    """ Executes the battle phase and returns the winner's name """
    input("Press any key to start the battle...")
    print('\n!Battle begins!\n')
    if (pokemons[0].get_hp() and pokemons[1].get_hp()):
        random.shuffle(pokemons)
        first_pokemon, second_pokemon = pokemons

        while True:
            first_pokemon.attack(second_pokemon)
            if second_pokemon.get_hp() <= 0:
                break
            second_pokemon.attack(first_pokemon)
            if first_pokemon.get_hp() <= 0:
                break
    
        if first_pokemon.get_hp() > second_pokemon.get_hp():
            return first_pokemon.get_name()
        elif first_pokemon.get_hp() < second_pokemon.get_hp():
            return second_pokemon.get_name()
        else:
            return ''
    else:
        return ''

def display_pokemon_cards(*args):
    for pokemon in args:
        pokemon.get_card()
        print()

def assign_pokemon_properties(**kwargs) -> Pokemon:
    """ Receives the details for each pokemon and creates the Pokemon objects """
    try:
        pokemon1_details = kwargs['pokemon1']
        pokemon2_details = kwargs['pokemon2']
    except KeyError as e:
        print("Incorrect key(s) provided")
    except Exception as e:
        print(e)
    else:
        pokemon1 = Pokemon(pokemon1_details)
        pokemon2 = Pokemon(pokemon2_details)
        return pokemon1, pokemon2
    return None
