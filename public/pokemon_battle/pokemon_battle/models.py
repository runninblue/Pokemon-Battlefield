import requests, random, math

class Pokemon:
    def __init__(self, id, name, stats, types, moves, abilities) -> None:
        self._id = id
        self._name = name.title()
        self._hp = self._process_stats(stats, 'hp')
        self._attack = self._process_stats(stats, 'attack')
        self._defense = self._process_stats(stats, 'defense')
        self._special_attack = self._process_stats(stats, 'special-attack')
        self._special_defense = self._process_stats(stats, 'special-defense')
        self._speed = self._process_stats(stats, 'speed')
        self._types = self._assign_types(self._process_properties(types, 'type'))
        self._moves = self._process_properties(moves, 'move')
        self._abilities = self._process_properties(abilities, 'ability')
        self._card = self.Card(self)

    def __str__(self) -> str:
        return f"{self._name}"        

    class Card:
        def __init__(self, obj) -> None:
            self._obj = obj

        def display_card(self) -> None:
            print(f"Card for {self._obj._name} (#{self._obj._id})")
            print(f"Type(s):", ', '.join(self._obj._types.keys()))
            print(f"HP: {self._obj._hp}")
            print(f"Attack stat: {self._obj._attack}")
            print(f"Defense stat: {self._obj._defense}")
            print(f"Special attack stat: {self._obj._special_attack}")
            print(f"Special defense stat: {self._obj._special_defense}")
            print(f"Speed: {self._obj._speed}")

    def _assign_types(self, types) -> dict:
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
        response = None
        while not response:
            move = random.choice(self._moves)
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
        response = None
        ability_desc = ''
        while not response:
            ability = random.choice(self._abilities)
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

    def _process_stats(self, stats, stat) -> int:
        result = [s for s in stats if s['stat']['name'] == stat]
        if result:
            return int(result[0]['base_stat'])
        else:
            return 0

    def _process_properties(self, properties, prop) -> list:
        properties_list = [{p[prop]['name'] : p[prop]['url']} for p in properties]
        if properties_list:
            return properties_list
        else:
            return list()

    def get_name(self) -> str:
        return self._name

    def get_card(self) -> None:
        self._card.display_card()
    
    def set_hp(self, hp) -> None:
        self._hp = hp

    def get_hp(self) -> int:
        return self._hp
    
    def get_attack_stat(self) -> int:
        return self._attack
    
    def get_defense_stat(self) -> int:
        return self._defense
    
    def get_types(self) -> dict:
        return self._types

    def _calculate_damage(self, move_power, opponent_defense) -> int:
        damage = (self._attack / max(1, opponent_defense)) * move_power
        return math.floor(damage / 2)

    def _calculate_attack_effectiveness(self, move_name, types, damage) -> int:
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
