import requests, random, math

class Pokemon:
    """ Pokemon class: assigns pokemon characteristics to variables """
    def __init__(self, id, name, stats, types, moves, abilities) -> None:
        self._ID = id
        self._NAME = name.title()
        self._hp = self._process_stats(stats, 'hp')
        self._ATTACK = self._process_stats(stats, 'attack')
        self._DEFENSE = self._process_stats(stats, 'defense')
        self._SPECIAL_ATTACK = self._process_stats(stats, 'special-attack')
        self._SPECIAL_DEFENSE = self._process_stats(stats, 'special-defense')
        self._SPEED = self._process_stats(stats, 'speed')
        self._TYPES = self._assign_types(self._process_properties(types, 'type'))
        self._MOVES = self._process_properties(moves, 'move')
        self._ABILITIES = self._process_properties(abilities, 'ability')
        self._CARD = self.Card(self)

    def __str__(self) -> str:
        return f"{self._name}"        

    class Card:
        """ Card class: Gets the pokemon object and prints on the screen its card """
        def __init__(self, obj) -> None:
            self._obj = obj

        def display_card(self) -> None:
            print(f"Card for {self._obj._NAME} (#{self._obj._ID})")
            print(f"Type(s):", ', '.join(self._obj._TYPES.keys()))
            print(f"HP: {self._obj._hp}")
            print(f"Attack stat: {self._obj._ATTACK}")
            print(f"Defense stat: {self._obj._DEFENSE}")
            print(f"Special attack stat: {self._obj._SPECIAL_ATTACK}")
            print(f"Special defense stat: {self._obj._SPECIAL_DEFENSE}")
            print(f"Speed: {self._obj._SPEED}")

    def _process_stats(self, stats, stat) -> int:
        """ This function receives the stats object and the stat name and returns the base_stat values for the stat """
        result = [s for s in stats if s['stat']['name'] == stat]
        if result:
            return int(result[0]['base_stat'])
        else:
            return 0

    def _process_properties(self, properties, prop) -> list:
        """ This functions receives an object (e.g. moves, abilities) and extracts the name and the url to fetch further details from the API """
        properties_list = [{p[prop]['name'] : p[prop]['url']} for p in properties]
        if properties_list:
            return properties_list
        else:
            return list()

    def _assign_types(self, types) -> dict:
        """ This function makes the necessary calls to the API to fetch the pokemon type details """
        type_properties = dict()
        for pok_type in types:
            for t in pok_type:
                data = {'url' : pok_type[t]}
                try:
                    response = requests.post('http://localhost:5000/type', data=data)
                except Exception as e:
                    print(e)
                    type_properties[t] = dict()
                else:
                    if response.ok:
                        type_properties[t] = response.json()
                    else:
                        type_properties[t] = dict()
        return type_properties

    def _get_move(self) -> tuple:
        """ This function chooses a random move from the list of moves available for each pokemon and makes the necessary call to the API to fetch its power value """
        response = None
        while not response:
            move = random.choice(self._MOVES)
            ((move_name, move_url),) = move.items()
            data = {'url' : move_url}
            try:
                res = requests.post('http://localhost:5000/move', data=data)
            except Exception as e:
                print(e)
            else:
                if res.ok:
                    response = res.json()
        else:
            move_power = response.get('power')
            if not move_power:
                move_power = 0
            return move_name, move_power

    def _get_ability(self) -> str:
        """ This function chooses a random ability from the list of abilities available for each pokemon and makes the necessary call to the API to fetch a short description """
        response = None
        ability_desc = ''
        while not response:
            ability = random.choice(self._ABILITIES)
            ((ability_name, ability_url),) = ability.items()
            data = {'url' : ability_url}
            try:
                res = requests.post('http://localhost:5000/ability', data=data)
            except Exception as e:
                print(e)
            else:
                if res.ok:
                    response = res.json()
        else:
            ability_desc = response.get('ability_desc')
            return ability_desc

    def get_name(self) -> str:
        return self._name

    def get_card(self) -> None:
        self._CARD.display_card()
    
    def set_hp(self, hp) -> None:
        self._hp = hp

    def get_hp(self) -> int:
        return self._hp
    
    def get_attack_stat(self) -> int:
        return self._ATTACK
    
    def get_defense_stat(self) -> int:
        return self._DEFENSE
    
    def get_types(self) -> dict:
        return self._TYPES

    def _calculate_damage(self, move_power, opponent_defense) -> int:
        """ This function implements a formula to calculate the damage caused by the selected move """
        damage = (self._ATTACK / max(1, opponent_defense)) * move_power
        return math.floor(damage / 2)

    def _calculate_attack_effectiveness(self, move_name, types, damage) -> int:
        """ This function adjusts the effectiveness of the damage based on pokemon type characteristics """
        for t in types:
            for relation in types[t]:
                if relation == 'double_damage_to' and move_name in types[t][relation]:
                    damage *= 2
                elif relation == 'half_damage_to' and move_name in types[t][relation]:
                    damage *= 0.5
                elif relation == 'no_damage_to' and move_name in types[t][relation]:
                    damage *= 0
        return math.floor(damage)

    def attack(self, opponent) -> None:
        """ This function implements the attack logic by calculating its potential damage and effectiveness.
            Then it decreases the opponent's health by the attack effectiveness value. """
        types = self.get_types()
        move_name, move_power = self._get_move()
        print(f"{self._name} attempts the {move_name} move against {opponent.get_name()}")
        damage = self._calculate_damage(move_power, opponent.get_defense_stat())
        attack_effectiveness = self._calculate_attack_effectiveness(move_name, types, damage)
        if attack_effectiveness > math.floor(opponent.get_hp() / 2):
            ability_desc = self._get_ability()
            print(f"{opponent.get_name()} {ability_desc.lower()}")
            attack_effectiveness = math.floor(attack_effectiveness / 4)
        print(f"Damage inflicted to {opponent.get_name()}: {attack_effectiveness}")
        opponent.set_hp(opponent.get_hp() - attack_effectiveness)
        print(f"{opponent.get_name()} HP: {opponent.get_hp()} - {self._name} HP: {self._hp}\n")
