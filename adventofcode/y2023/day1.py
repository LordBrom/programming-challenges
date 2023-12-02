
def part1(data, test=False) -> str:
    first = -1
    last = 0
    sum = 0
    for word in data:
        first = -1
        for n in word:
            if n.isnumeric():
                if first == -1:
                    first = n
                last = n
        sum += int(str(first) + str(last))
    return str(sum)


def part2(data, test=False) -> str:
    first = -1
    last = 0
    sum = 0
    num_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for word in data:
        first = -1
        for i,n in enumerate(word):
            if n.isnumeric():
                if first == -1:
                    first = n
                last = n
            else:
                for num_pos, num in enumerate(num_strs):
                    if word[i:i + len(num)] == num:
                        if first == -1:
                            first = num_pos + 1
                        last = num_pos + 1
                        break
        sum += int(str(first) + str(last))
    return str(sum)
