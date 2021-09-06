"""
ID: mills.n2
LANG: PYTHON3
TASK: gift1
"""

import math

inFile = open("gift1.in", "r").read().split("\n")
inFile.pop()
outFile = open("gift1.out", "w")

numOfGifters = int(inFile.pop(0))
namesOfGifters = []
moneyOfGifters = []
gifters = {}

for i in range(numOfGifters):
	gifters[inFile.pop(0)] = 0

for i in range(numOfGifters):
	thisGifter = inFile.pop(0)
	gifterMoneyLine = inFile.pop(0).split(" ")
	gifterMoney = int(gifterMoneyLine[0])
	gifts = int(gifterMoneyLine[1])

	if gifts != 0:
		giftValue = math.floor(gifterMoney / gifts)
		giftValueRemainder = gifterMoney - (giftValue * gifts)
		gifters[thisGifter] += (-1 * gifterMoney) + giftValueRemainder
		for g in range(gifts):
			giftiee = inFile.pop(0)
			gifters[giftiee] += giftValue

for i in gifters:
	outFile.write(i + " " + str(gifters[i]) + "\n")

outFile.close()
