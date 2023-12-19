from models import Pokemon

def battle(pokemon1, pokemon2) -> str:
    """ This function shows the pokemon cards, proceeds with the attack phase and returns the winner's name """
    pokemon1.get_card()
    print()
    pokemon2.get_card()
    input("\nPress any key to start the battle...")
    print('\n!Battle begins!\n')
    while True:
        pokemon1.attack(pokemon2)
        if pokemon2.get_hp() <= 0:
            break
        pokemon2.attack(pokemon1)
        if pokemon1.get_hp() <= 0:
            break
    
    if pokemon1.get_hp() > pokemon2.get_hp():
        return pokemon1.get_name()
    elif pokemon1.get_hp() < pokemon2.get_hp():
        return pokemon2.get_name()
    else:
        return ''

def assign_pokemon_properties(**kwargs) -> Pokemon:
    """ This function receives the details for each pokemon and creates the Pokemon objects """
    try:
        pokemon1_details = kwargs['pokemon1']
        pokemon2_details = kwargs['pokemon2']
    except KeyError as e:
        print("Incorrect keys provided")
        return None
    except Exception as e:
        print(e)
        return None
    else:
        pokemon1 = Pokemon(pokemon1_details)
        pokemon2 = Pokemon(pokemon2_details)
        return pokemon1, pokemon2
