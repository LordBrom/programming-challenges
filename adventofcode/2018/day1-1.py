inFile = open("day1.in", "r").read().split("\n")
inFile.pop()

result = 0

for i in inFile:
    result += int(i)

print(result)
