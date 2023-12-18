import requests, sys
from battle import assign_pokemon_properties, battle

def validate_contesters(pok1, pok2) -> dict | None:
    """ This function validates the contester names via the API. If a pokemon name is found it returns its details, otherwise it returns None """
    data = {'pokemon1' : pok1, 'pokemon2' : pok2}
    try:
        response = requests.post("http://localhost:5000", data=data)
        if response.ok:
            return response.json()
        else:
            return None
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    contester_details = None
    # Checks if pokemon names are provided as arguments
    args = sys.argv[1:]
    if args:
        if len(args) > 2:
            args = args[:2]
        contester_details = validate_contesters(args[0], args[1])

    # While contester details fail to be retrieved from the API user should provide the names through input
    while not contester_details:
        print("\n---- POKEMON BATTLE ----\n")
        pokemon1 = input("Provide the name of the first contester: ")
        pokemon2 = input("Provide the name of the second contester: ")
        contester_details = validate_contesters(pokemon1, pokemon2)
    else:
        pokemon1, pokemon2 = assign_pokemon_properties(pokemon1 = contester_details['pokemon1'], pokemon2 = contester_details['pokemon2'])
        winner = battle(pokemon1, pokemon2)
        if winner:
            print(f"{winner} wins!")
        else:
            print("!It's a draw!")
        