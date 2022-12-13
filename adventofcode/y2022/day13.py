import json
from functools import cmp_to_key

def compare_packets(leftPacket, rightPacket):
	if isinstance(leftPacket, int) and isinstance(rightPacket, int):
		return leftPacket <= rightPacket

	elif not isinstance(leftPacket, int) and not isinstance(rightPacket, int):
		for i in range(len(leftPacket)):
			if i >= len(rightPacket):
				return False
			if leftPacket[i] != rightPacket[i]:
				return compare_packets(leftPacket=leftPacket[i], rightPacket=rightPacket[i])

	elif isinstance(leftPacket, int):
		if not compare_packets(leftPacket=[leftPacket], rightPacket=rightPacket):
			return False

	elif isinstance(rightPacket, int):
		if not compare_packets(leftPacket=leftPacket, rightPacket=[rightPacket]):
			return False

	return True

def sort_packet(leftPacket, rightPacket):
	if compare_packets(leftPacket, rightPacket):
		return -1
	return 1

def part1(data, test=False) -> str:
	leftPacket = None
	rightPacket = None
	index = 1
	result = 0
	while len(data):
		leftPacket = json.loads(data.pop(0))
		rightPacket = json.loads(data.pop(0))
		if len(data):
			data.pop(0)
		if compare_packets(leftPacket, rightPacket):
			result += index
		index += 1
	return str(result)


def part2(data, test=False) -> str:
	packetList = []
	packetList.append(json.loads('[[2]]'))
	packetList.append(json.loads('[[6]]'))

	for d in data:
		if len(d):
			packetList.append(json.loads(d))

	packetList.sort(key=cmp_to_key(sort_packet))
	packetList.sort(key=cmp_to_key(sort_packet))

	keyPos1 = packetList.index(json.loads('[[2]]')) + 1
	keyPos2 = packetList.index(json.loads('[[6]]')) + 1

	return str(keyPos1 * keyPos2)
