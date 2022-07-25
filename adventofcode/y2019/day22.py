import math


def shuffle_deck(shuffleOrder, deck):
    for shuffle in shuffleOrder:
        shuffleSplit = shuffle.split(" ")
        if shuffle == "deal into new stack":
            deck = deck[::-1]
        elif shuffleSplit[0] == "cut":
            pos = int(shuffleSplit[1])
            deck = deck[pos:] + deck[:pos]
        else:
            increment = int(shuffleSplit[-1])
            pos = 0
            newDeck = deck.copy()
            while len(deck) > 0:
                newDeck[pos] = deck.pop(0)
                pos += increment
                pos %= len(newDeck)
            deck = newDeck
    return deck


def part1(data, test=False) -> str:
    deck = list(range(10007))
    if test:
        deck = list(range(10))
    deck = shuffle_deck(data, deck)

    if test:
        return str(deck)
    else:
        for i, c in enumerate(deck):
            if c == 2019:
                return str(i)
    return ""


def part2(data, test=False) -> str:
    deck = list(range(10007))
    if test:
        deck = list(range(10))

    decks = []

    for i in range(101741582076661 % math.floor(len(deck) / 2)):
        deck = shuffle_deck(data, deck.copy())
        if i % 10 == 0:
            print("here")
        if deck in decks:
            print(deck)
            print(i)
            input()
        else:
            decks.append(deck.copy())
        # print(deck)
        # input()

    if test:
        return str(deck)
    else:
        return str(deck[2020])
