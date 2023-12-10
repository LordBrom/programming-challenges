
def process_line(nums):

    all_same = True
    for num in nums:
        if num != nums[0]:
            all_same = False

    if all_same:
        return nums[0], nums[0]

    new_nums = []
    for i,_ in enumerate(nums):
        if i == len(nums) - 1:
            break
        new_nums.append(nums[i + 1] - nums[i])

    next_line = process_line(new_nums)

    return (nums[-1] + next_line[0], nums[0] - next_line[1])

def part1(data, test=False) -> str:
    result = 0
    for line in data:
        result += process_line([int(x) for x in line.split(" ")])[0]
    return str((result))


def part2(data, test=False) -> str:
    result = 0
    for line in data:
        result += process_line([int(x) for x in line.split(" ")])[1]
    return str((result))
