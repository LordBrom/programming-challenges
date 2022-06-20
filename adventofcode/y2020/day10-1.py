def check_charge(adapters, charge, checked):
    checked.append(charge)

    result = checked

    for offset in [1, 3]:
        check = charge + offset

        if check in checked:
            continue
        elif check < 0:
            continue
        elif check >= len(adapters):
            continue
        elif adapters[check]:
            newResult = check_charge(adapters, check, checked)
            if len(newResult) > len(result):
                result = newResult
    return result


inFile = open("day10.in", "r").read().split("\n")
inFile.pop()

intFile = [int(x) for x in inFile]
intFile.sort()

adapters = [True]

for i in range(int(intFile[len(intFile) - 1]) + 3):
    if i == 0:
        continue
    if i in intFile:
        adapters.append(True)
    else:
        adapters.append(False)
adapters.append(True)

checkResult = check_charge(adapters, 0, [])

result1 = 0
result3 = 0
for i in range(len(checkResult) - 1):
    if abs(checkResult[i + 1] - checkResult[i]) == 1:
        result1 += 1
    elif abs(checkResult[i + 1] - checkResult[i]) == 3:
        result3 += 1

print(result1 * result3)
