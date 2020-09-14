# P178
#Card
#http://tinyurl.com/jj22qv4

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2","3","4","5","6","7","8","9",
              "10","Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        """スート(マーク)も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2:
                return True
        else:
            return False
        return False

    def __gt__(self, c2):
        if self.value > c2.suit:
            return True
        if self.value == c2.suit:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of "\
            + self.suits[self.suit]
        return v

# P180
# http://tinyurl.com/j6donnr

card1 = Card(10,2)
card2 = Card(11,3)
print(card1 < card2)

# http://tinyurl.com/hc9ktlr

card1 = Card(10,2)
card2 = Card(11,3)
print(card1 > card2)

# http://tinyurl.com/z57hc75

card = Card(3,2)
print(card)

# P181
# Deck
# http://tinyurl.com/jz8zfz7

from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# P182
# http://tinyurl.com/hsv5n6p

deck = Deck()
for card in deck.cards:
    print(card)

# Player
# http://tinyurl.com/gwyrt2s

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

# Game
# http://tinyurl.com/huwq8mw

class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前")
        name2 = input("プレーヤー2の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "このラウンドは {} が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} は {}、{} は {} を引きました"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでplay:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p2.name)
        print("ゲーム終了、{} の勝利です！".format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return  p1.name
        if p1.wins < p2.wins:
            return  p2.name
        return "引き分け！"