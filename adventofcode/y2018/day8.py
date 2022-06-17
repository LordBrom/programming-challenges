def parseNavigationNodes(inData, part2=False, depth=1):
    childCount = int(inData.pop(0))
    metaDataCount = int(inData.pop(0))
    metaDataSum = 0

    childMetaData = []
    for i in range(childCount):
        newMetaData, inData = parseNavigationNodes(inData.copy(), part2, depth + 1)
        childMetaData.append(newMetaData)
        if not part2:
            metaDataSum += newMetaData

    for i in range(metaDataCount):
        if part2 and childCount > 0:
            metaDataPosition = int(inData.pop(0)) - 1
            if len(childMetaData) > metaDataPosition:
                metaDataSum += childMetaData[metaDataPosition]
            pass
        else:
            metaDataSum += int(inData.pop(0))

    return metaDataSum, inData


def part1(data, test=False) -> str:
    data = data[0]
    result = parseNavigationNodes(data.split(" "))
    return str(result[0])


def part2(data, test=False) -> str:
    data = data[0]
    result = parseNavigationNodes(data.split(" "), True)
    return str(result[0])
