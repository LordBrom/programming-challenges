
def part1(data, test=False) -> str:
    result = 0
    colors = {'red':12,'green':13,'blue':14}
    for i,game in enumerate(data):
        start = game.find(":")
        rounds = game[start + 2:].split("; ")
        for round in rounds:
            draws = round.split(", ")
            valid = True
            for draw in draws:
                num, color = draw.split(" ")
                if (colors[color] < int(num)):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            result += i + 1

    return str(result)


def part2(data, test=False) -> str:
    result = 0
    for i,game in enumerate(data):
        colors = {'red':0,'green':0,'blue':0}
        start = game.find(":")
        rounds = game[start + 2:].split("; ")
        for round in rounds:
            draws = round.split(", ")
            for draw in draws:
                num, color = draw.split(" ")
                colors[color] = max(colors[color], int(num))
        result += (colors['red'] * colors['green'] * colors['blue'])
    return str(result)
