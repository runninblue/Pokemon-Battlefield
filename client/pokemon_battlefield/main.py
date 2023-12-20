import requests, sys
from battle import *
from exceptions import *

def validate_contesters(pok1, pok2) -> dict | None:
    """ Validates the contester names via the API.
    If a pokemon name is found it returns its details, otherwise it returns None """

    data = {'pokemon1' : pok1, 'pokemon2' : pok2}
    try:
        response = requests.post("http://localhost:5000", data=data)
        if response.ok:
            return response.json()
        else:
            raise PokemonValidationException()
    except PokemonValidationException as e:
        print(e)
    except Exception as e:
        print(e)
    return None

def parse_args():
    """ Checks if pokemon names are provided as arguments and if not it raises an exception """
    args = sys.argv[1:]
    if args:
        try:
            if len(args) >= 2:
                args = args[:2]
                validated_contesters = validate_contesters(args[0], args[1])
                sys.argv = [sys.argv[0]]
                return validated_contesters
            else:
                raise PokemonNamesNumberException()
        except PokemonNamesNumberException as e:
            print(e)
        except Exception as e:
            print(e)
        return None
    else:
        return None

def main():
    contester_details = None
    contester_details = parse_args()

    # While contester details fail to be retrieved from the API user should provide the names through input
    while not contester_details:
        print("\n---- POKEMON BATTLEFIELD ----")
        print("Author: E.H.\n")
        pokemon1_name = input("Choose first Pokemon: ")
        pokemon2_name = input("Choose second Pokemon: ")
        if pokemon1_name and pokemon2_name:
            contester_details = validate_contesters(pokemon1_name, pokemon2_name)
    else:
        try:
            pokemons = assign_pokemon_properties(pokemon1 = contester_details['pokemon1'], pokemon2 = contester_details['pokemon2'])
            if pokemons:
                pokemons = list(pokemons)
                display_pokemon_cards(pokemons)
                winner = battle(pokemons)
                if winner:
                    print(f"{winner} wins!")
                else:
                    print("!No Pokemon has won!")
            else:
                raise PokemonSelectionException()
        except PokemonSelectionException as e:
            print("Pokemons cannot be selected for battle")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # Initiates the main function and prompts user to rerun it upon completion
    main()
    while input("\n\nPlay again? (y/n): ").lower() == 'y':
        main()
    else:
        sys.exit(0)