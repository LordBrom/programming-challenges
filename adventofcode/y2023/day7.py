
from sys import maxsize

class Hand():
    def __init__(self, hand, bid, part2 = False) -> None:
        self.part2 = part2
        self.hand = hand
        self.bid = bid
        self.handRank = self.get_rank()

    def __str__(self) -> str:
        return self.hand + " " + str(self.handRank)

    def __lt__(self, __o: 'Hand') -> bool:
        if self.handRank == __o.handRank:
            return not self.compare_hands(__o.hand)
        return self.handRank < __o.handRank

    def compare_hands(self, other):
        if self.part2:
            card_ranking = {
                'A':12, 'K':11, 'Q':10, 'J':-1, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0
            }
        else:
            card_ranking = {
                'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0
            }
        hand_score = [card_ranking[card] for card in self.hand]
        other_score = [card_ranking[card] for card in other]
        for i,score in enumerate(hand_score):
            if score == other_score[i]:
                continue
            return score > other_score[i]

        return True

    def get_rank(self):
        types = {}
        jokers = 0
        for card in self.hand:
            if self.part2 and card == "J":
                jokers += 1
                continue
            if not card in types:
                types[card] = 0
            types[card] += 1

        highCount = 0
        lowCount = maxsize
        countPairs = 0
        for type in types:
            if types[type] == 2:
                countPairs += 1
            highCount = max(highCount, types[type])
            lowCount = min(lowCount, types[type])

        if highCount + jokers == 5:
            return 7
        if highCount + jokers == 4:
            return 6
        if (highCount == 3 and lowCount == 2) or (countPairs == 2 and jokers == 1):
            return 5
        if highCount + jokers == 3:
            return 4
        if countPairs == 2:
            return 3
        if highCount + jokers == 2:
            return 2
        if highCount + jokers == 1:
            return 1


def parse_hands(data, part2 = False):
    hands = []
    for line in data:
        lineSplit = line.split(" ")
        hands.append(Hand(lineSplit[0], lineSplit[1], part2))

    return hands

def part1(data, test=False) -> str:
    hands = parse_hands(data)
    hands.sort()

    result = 0
    for i,hand in enumerate(hands):
        result += int(hand.bid) * (i + 1)

    return str(result)


def part2(data, test=False) -> str:
    hands = parse_hands(data, True)
    hands.sort()

    result = 0
    for i,hand in enumerate(hands):
        result += int(hand.bid) * (i + 1)

    return str(result)
