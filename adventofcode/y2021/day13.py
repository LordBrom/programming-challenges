def parseInput(data):
    points = []
    folds = []

    for i in data:
        if len(i) == 0:
            continue
        if i[0] == "f":
            folds.append(i.split("along ")[1].split("="))
        else:
            points.append(i.split(","))
    return [points, folds]


def makeFold(paper, fold):

    for x in range(len(paper)):
        if fold[0] == "y" and x > ((len(paper) - 1) / 2):
            break

        for y in range(len(paper[x])):
            if fold[0] == "x" and y > ((len(paper[x]) - 1) / 2):
                break
            if fold[0] == "x":
                paper[x][y] = paper[x][y] or paper[x][(int(fold[1]) - y) + int(fold[1])]
            else:
                paper[x][y] = paper[x][y] or paper[(int(fold[1]) - x) + int(fold[1])][y]

    if fold[0] == "y":
        del paper[int(fold[1]) :]
    else:
        for x in range(len(paper)):
            del paper[x][int(fold[1]) :]

    return paper


def countMarks(paper):
    result = 0
    for x in range(len(paper)):
        for y in range(len(paper[x])):
            if paper[x][y]:
                result += 1
    return result


def printPaper(paper):
    for x in range(len(paper)):
        rowStr = ""
        for y in range(len(paper[x])):
            if paper[x][y]:
                rowStr += " #"
            else:
                rowStr += " ."
        print(rowStr)


def part1(data, test=False) -> str:
    paper = []
    paperSize = 1500
    for x in range(paperSize):
        paper.append([False for x in range(paperSize)])

    dataParsed = parseInput(data)

    for point in dataParsed[0]:
        paper[int(point[1])][int(point[0])] = True

    paper = makeFold(paper, dataParsed[1][0])

    return countMarks(paper)


def part2(data, test=False) -> str:
    paper = []
    paperSize = 1500
    for x in range(paperSize):
        paper.append([False for x in range(paperSize)])

    dataParsed = parseInput(data)

    for point in dataParsed[0]:
        paper[int(point[1])][int(point[0])] = True

    for fold in dataParsed[1]:
        paper = makeFold(paper, fold)

    printPaper(paper)
    return "See Above"
