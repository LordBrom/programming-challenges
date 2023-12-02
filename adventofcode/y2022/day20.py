
class EncryptNum():

	def __init__(self, num, turn, total) -> None:
		self.num = num
		self.turn = turn
		self.total = total
		self.next = None
		self.prev = None

	def to_string(self, len):
		if len == 0:
			return ""
		return str(self.num) + " " + self.next.to_string(len - 1)

	def get_next(self, i, depth = 0):
		if i == 0:
			return self
		return eval(f"self{'.next' * i}")

	def get_prev(self, i):
		if i == 0:
			return self
		return eval(f"self{'.prev' * i}")

	def move(self):
		if self.num > 0:
			newPrev = self.get_next(self.num % self.total)
		else:
			newPrev = self.get_prev(abs((self.num - 1) ) % self.total)
		#print(newPrev.num)
		#input()

		oldNext = self.next
		self.next.prev = self.prev
		self.prev.next = oldNext

		self.prev = newPrev
		self.next = newPrev.next
		self.next.prev = self
		self.prev.next = self

def build_queue(data):
	queue = []
	prevNum = None
	zeroIndex = None
	for i,d in enumerate(data):
		nextNum = EncryptNum(int(d), i, len(data))
		if int(d) == 0:
			zeroIndex = i

		if len(queue):
			nextNum.prev = queue[-1]
			queue[-1].next = nextNum

		if prevNum != None:
			prevNum.next = nextNum
			nextNum.prev = prevNum
		prevNum = nextNum
		queue.append(nextNum)
	queue[0].prev = queue[-1]
	queue[-1].next = queue[0]

	return queue, zeroIndex


def decrypt(nums, cycles = 1):
	idxs = [*range(len(nums))]

	for i in idxs * cycles:
		j = idxs.index(i)
		idxs.pop(j)
		idxs.insert((j + nums[i]) % len(idxs), i)

	zeroPos = idxs.index(nums.index(0))
	result = 0
	result += nums[idxs[(zeroPos + 1000) % len(nums)]]
	result += nums[idxs[(zeroPos + 2000) % len(nums)]]
	result += nums[idxs[(zeroPos + 3000) % len(nums)]]
	return result


def part1(data, test=False) -> str:
	nums = [int(x) for x in data]
	return str(decrypt(nums))


	queue, zeroIndex = build_queue(data)

	for i in range(len(data)):
		try:
			#print(queue[zeroIndex].to_string(7))
			queue[i].move()
		except Exception as e:
			print(e)

	#print(queue[zeroIndex].to_string(7))
	num1 = queue[zeroIndex].get_next(1000 % len(data))
	num2 = num1.get_next(1000 % len(data))
	num3 = num2.get_next(1000 % len(data))
	print(num1.num, num2.num, num3.num)
	return str(num1.num + num2.num + num3.num)

	#6932 - low
	#11286 - high


def part2(data, test=False) -> str:
	nums = [int(x) * 811589153 for x in data]
	return str(decrypt(nums, 10))
