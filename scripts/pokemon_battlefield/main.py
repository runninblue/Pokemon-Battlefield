import requests, sys
from battle import *
from exceptions import *

def validate_contesters(pok1, pok2) -> dict | None:
    """ This function validates the contester names via the API. If a pokemon name is found it returns its details, otherwise it returns None """
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
    # Checks if pokemon names are provided as arguments and if not it raises an exception
    args = sys.argv[1:]
    if args:
        try:
            if len(args) >= 2:
                args = args[:2]
                validated_contesters = validate_contesters(args[0], args[1])
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
        print("\n---- POKEMON BATTLE ----\n")
        pokemon1_name = input("Provide the name of the first contester: ")
        pokemon2_name = input("Provide the name of the second contester: ")
        if pokemon1_name and pokemon2_name:
            contester_details = validate_contesters(pokemon1_name, pokemon2_name)
    else:
        try:
            pokemons = assign_pokemon_properties(pokemon1 = contester_details['pokemon1'], pokemon2 = contester_details['pokemon2'])
            if pokemons:
                display_pokemon_cards(pokemons[0], pokemons[1])
                winner = battle(pokemons[0], pokemons[1])
                if winner:
                    print(f"{winner} wins!")
                else:
                    print("!It's a draw!")
            else:
                raise PokemonSelectionException()
        except PokemonSelectionException as e:
            print("Pokemons cannot be selected for battle")
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)
        finally:
            sys.exit(0)

if __name__ == "__main__":
    main()