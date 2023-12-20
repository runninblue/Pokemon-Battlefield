import unittest
import random
from unittest.mock import patch
from battle import battle
from models import Pokemon

class TestBattleFunction(unittest.TestCase):
    @patch('builtins.input', return_value='\n')
    @patch('random.choice', side_effect=lambda x: random.choice(x))
    @patch('random.shuffle', side_effect=lambda x: random.sample(x, len(x)))
    def test_battle_winner_random(self, mock_input, mock_random_choice, mock_random_shuffle):
        # Tests if it returns either Pokemon as winner
        pokemons = [Pokemon({'name': 'pokemon1', 'hp': 50, 'attack': 10, 'defense' : 100}),
                    Pokemon({'name': 'pokemon2', 'hp': 100, 'attack': 8, 'defense' : 20})]
        winner = battle(pokemons)
        self.assertIn(winner, ['Pokemon1', 'Pokemon2'])
        self.assertIsInstance(winner, str)

    @patch('builtins.input', return_value='\n')
    @patch('random.choice', side_effect=lambda x: random.choice(x))
    @patch('random.shuffle', side_effect=lambda x: random.shuffle(x))
    def test_battle_winner_no_hp(self, mock_input, mock_random_choice, mock_random_shuffle):
        # Tests behaviour if no hp is provided
        pokemons = [Pokemon({'name': 'pokemon1', 'hp': 0}),
                    Pokemon({'name': 'pokemon2', 'hp': 0})]
        winner = battle(pokemons)
        self.assertEqual(winner, '')

if __name__ == '__main__':
    unittest.main()
