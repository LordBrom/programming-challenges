inFile = open("day1.in", "r").read().split("\n")
inFile.pop()

result = 0

found = {}
i = 0


while True:
    result += int(inFile[i % len(inFile)])
    i += 1
    try:
        if found[result]:
            print(result)
            break
    except:
        found[result] = True
