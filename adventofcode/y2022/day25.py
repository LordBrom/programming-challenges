
def convert_from_snafu(snafu):
	reverse = snafu[::-1]
	dec = 0
	for i,n in enumerate(reverse):
		if n in ['0','1','2']:
			dec += int(n) * 5**i
		elif n == "-":
			dec += -1 * 5**i
		elif n == "=":
			dec += -2 * 5**i
	return dec

def convert_to_snafu(dec):
	snafu = [0]
	while dec > 0:
		dig = int(dec % 5)
		snafu[-1] += dig
		if snafu[-1] == 3:
			snafu[-1] = "="
			snafu.append(1)
		elif snafu[-1] == 4:
			snafu[-1] = "-"
			snafu.append(1)
		elif snafu[-1] == 5:
			snafu[-1] = "0"
			snafu.append(1)
		else:
			snafu.append(0)
		dec //= 5
	if snafu[-1] == 0:
		snafu.pop()
	return ''.join([str(n) for n in snafu])[::-1]

def part1(data, test=False) -> str:
	result = 0
	for d in data:
		s = convert_from_snafu(d)
		bd = convert_to_snafu(s)
		if d != bd:
			print(d, "||", s, "||", bd)
		result += convert_from_snafu(d)
	return convert_to_snafu(result)

def part2(data, test=False) -> str:
	return "Merry Christmas"
