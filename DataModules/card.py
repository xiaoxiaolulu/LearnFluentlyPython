import collections

Card = collections.namedtuple('card', ['rank', 'suit'])


class FrenchDeck:

    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    from random import choice

    print(choice(deck))

    for card in deck:
        print(card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    def spades_high(card):
        rank_value = FrenchDeck.rank.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)