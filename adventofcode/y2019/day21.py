from y2019.intcode import AsciiComputer


def part1(data, test=False) -> str:

    comp = AsciiComputer(data[0].split(","))

    comp.append_input("NOT C J")
    comp.append_input("NOT B T")
    comp.append_input("OR T J")
    comp.append_input("NOT A T")
    comp.append_input("OR T J")

    comp.append_input("NOT D T")
    comp.append_input("NOT J J")
    comp.append_input("OR J T")
    comp.append_input("NOT T J")

    comp.append_input("WALK")

    ascii, result = comp.run()

    if test:
        print(ascii)

    return str(result[-1])


def part2(data, test=False) -> str:

    comp = AsciiComputer(data[0].split(","))

    comp.append_input("NOT C J")
    comp.append_input("NOT B T")
    comp.append_input("OR T J")
    comp.append_input("NOT A T")
    comp.append_input("OR T J")

    comp.append_input("NOT J J")

    comp.append_input("NOT D T")
    comp.append_input("OR T J")

    comp.append_input("NOT E T")
    comp.append_input("NOT T T")
    comp.append_input("OR H T")
    comp.append_input("NOT T T")
    comp.append_input("OR T J")

    comp.append_input("NOT J J")

    comp.append_input("RUN")

    ascii, result = comp.run()

    if test:
        print(ascii)

    return str(result[-1])
