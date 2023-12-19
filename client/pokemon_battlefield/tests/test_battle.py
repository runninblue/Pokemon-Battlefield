import unittest
from unittest.mock import patch
import random
from battle import battle
from models import Pokemon

class TestBattleFunction(unittest.TestCase):
    @patch('builtins.input', return_value='\n')
    @patch('random.choice', side_effect=lambda x: random.choice(x))
    def test_battle_winner_random(self, mock_input, mock_random_choice):
        pokemon1 = Pokemon({'name': 'pokemon1', 'hp': 50, 'attack': 10, 'defense' : 100})
        pokemon2 = Pokemon({'name': 'pokemon2', 'hp': 100, 'attack': 8, 'defense' : 20})
        winner = battle(pokemon1, pokemon2)
        self.assertIn(winner, ['Pokemon1', 'Pokemon2'])

    @patch('builtins.input', return_value='\n')
    @patch('random.choice', side_effect=lambda x: random.choice(x))
    def test_battle_winner_no_hp(self, mock_input, mock_random_choice):
        pokemon1 = Pokemon({'name': 'pokemon1', 'hp': 0})
        pokemon2 = Pokemon({'name': 'pokemon2', 'hp': 0})
        winner = battle(pokemon1, pokemon2)
        self.assertEqual(winner, '')

if __name__ == '__main__':
    unittest.main()
