from card import Card


class Hand:
    def __init__(self, cards):
        self.max_size = 10
        self.cards = []

    def add_card(self, card):
        if len(self.cards) == self.max_size:
            return None
        else:
            self.cards.append(Card)

    def remove_card(self, id):
        return [c for c in self.alive_cards() if c.taunt]

    def find_card_index_by_id(self, searched_card_id):
        index = 0
        for card in self.cards:
            if card.id == searched_card_id:
                return index
            index += 1

    def get_new_id(self):
        if len([ c.id for c in self.cards ]) > 0:
            return max([ c.id for c in self.cards ]) + 1
        else:
            return 1000

    def insert_by_index(self, card, index):
        if index < 0:
            # Don't do anything
            pass
        elif index > self.max_size:
           pass
        else:
            self.cards.insert(index, card)

    def add(self, card, at_index):
        id = self.get_new_id()
        card.id = id
        self.insert_by_index(card, at_index)

    def remove(self, card: Card) -> int:
        card_index = self.find_card_index_by_id(card.id)
        del self.cards[card_index]

        if card_index < self.attacker_index:
            self.attacker_index -= 1
        if self.attacker_index == card_index and len(self.cards) > 0:
            self.attacker_index %= len(self.cards)

        return card_index

    def get_string(self, debug=False):
        return '  ||  '.join([ c.get_stats_str(debug) for c in self.alive_cards() ])

    def reset(self):
        self.cards = []
