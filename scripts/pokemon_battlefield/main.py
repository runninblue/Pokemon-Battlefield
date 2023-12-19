import requests, sys
from battle import assign_pokemon_properties, battle
from exceptions import PokemonNamesException, PokemonValidationException, PokemonSelectionException

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
        return None
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    contester_details = None
    # Checks if pokemon names are provided as arguments and if not it raises an exception
    args = sys.argv[1:]
    try:
        if args:
            if len(args) >= 2:
                args = args[:2]
                contester_details = validate_contesters(args[0], args[1])
            else:
                raise PokemonNamesException()
    except PokemonNamesException as e:
        pass
    except Exception as e:
        print(e)

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