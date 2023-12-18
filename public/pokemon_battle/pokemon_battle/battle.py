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
    pokemon1 = kwargs['pokemon1']
    pokemon2 = kwargs['pokemon2']
    pokemon1 = Pokemon(pokemon1['id'], pokemon1['name'], pokemon1['stats'], pokemon1['types'], pokemon1['moves'], pokemon1['abilities'])
    pokemon2 = Pokemon(pokemon2['id'], pokemon2['name'], pokemon2['stats'], pokemon2['types'], pokemon2['moves'], pokemon2['abilities'])
    return pokemon1, pokemon2
