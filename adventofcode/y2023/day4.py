
def score_card(card, part2 = False):
    score = 0
    for num in card[1]:
        if num in card[0]:
            if score == 0:
                score = 1
            elif part2:
                score += 1
            else:
                score *= 2
    return score

def parse_cards(data):
    cards = []
    for line in data:
        numbers = line.split(": ")[1]
        numbers = numbers.replace("  ", " ")
        num_split = numbers.split(" | ")
        winningNumbers = [int(x) for x in num_split[0].strip().split(" ")]
        cardNumbers = [int(x) for x in num_split[1].strip().split(" ")]
        cards.append((winningNumbers, cardNumbers))
    return cards

def part1(data, test=False) -> str:
    cards = parse_cards(data)
    result = 0
    for card in cards:
        result += score_card(card)
    return str(result)


def part2(data, test=False) -> str:
    cards = parse_cards(data)
    results = [1 for _ in cards]
    for i,card in enumerate(cards):
        wins = score_card(card, True)
        for n in range(i + 1, min(i + 1 + wins, len(cards))):
            results[n] += results[i]
    return str(sum(results))
