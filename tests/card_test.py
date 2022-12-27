import unittest
from card import Card
from deathrattle.summon import Summon


class TestCard(unittest.TestCase):
    def test_create_card(self):
        card = Card(
            name="minion",
            attack=3,
            hit_points=4,
            taunt=True,
            divine_shield=True,
            poisonous=True,
            deathrattle=Summon(Card("tabycat", 1, 1))
        )

        self.assertEqual(card.name, "minion")
        self.assertEqual(card.attack, 3)
        self.assertEqual(card.hit_points, 4)
        self.assertEqual(card.taunt, True)
        self.assertEqual(card.divine_shield, True)
        self.assertEqual(card.poisonous, True)
        self.assertEqual(card.is_alive, True)


    def test_take_damage_survives(self):
        card = Card("minion", 3, 3)
        card.take_damage(1)
        self.assertEqual(card.life, 2)
        self.assertEqual(card.is_alive, True)


    def test_take_damage_dies(self):
        card = Card("minion", 3, 3)
        card.take_damage(3)
        self.assertEqual(card.life, 0)
        self.assertEqual(card.is_alive, False)


    def test_take_damage_with_divine_shield(self):
        card = Card("minion", 3, 3, divine_shield=True)
        card.take_damage(1)
        self.assertEqual(card.life, 3)
        self.assertEqual(card.is_alive, True)
        self.assertEqual(card.divine_shield, False)


    def test_take_damage_with_poison(self):
        card = Card("minion", 3, 3)
        card.take_damage(1, poison=True)
        self.assertEqual(card.life, 0)
        self.assertEqual(card.is_alive, False)


    def test_take_damage_with_poison_and_divine_shield(self):
        card = Card("minion", 3, 3, divine_shield=True)
        card.take_damage(1, poison=True)
        self.assertEqual(card.life, 3)
        self.assertEqual(card.is_alive, True)
        self.assertEqual(card.divine_shield, False)
