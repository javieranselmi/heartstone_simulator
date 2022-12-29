from unittest import TestCase

from card import Card
from deck import Deck


class TestDeck(TestCase):
    def test_get_next_attacker(self):
        deck = Deck([Card("minion1", 3, 3), Card("minion2", 3, 3)])
        attacker1 = deck.get_next_attacker()
        self.assertEqual(attacker1.name,  "minion1")

        attacker2 = deck.get_next_attacker()
        self.assertEqual(attacker2.name,  "minion2")

    def test_get_next_attacker_skip_dead_minion(self):
        deck = Deck([
            Card("minion1", 3, 3),
            Card("minion2", 3, 3, taunt=True),
            Card("minion3", 3, 3),
        ])

        minion2 = deck.get_defender()
        minion2.take_damage(3)

        attacker1 = deck.get_next_attacker()
        self.assertEqual(attacker1.name,  "minion1")

        attacker2 = deck.get_next_attacker()
        self.assertEqual(attacker2.name,  "minion3")
