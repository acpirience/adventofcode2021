from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/2#part2
    """
    day = "2"
    part = "2"

    logger.info(f"Day {day} part {part}")

    pos = 0
    depth = 0
    aim = 0
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            instruction, amount = line.split(" ")
            if instruction == "forward":
                pos += int(amount)
                depth += aim * int(amount)
            if instruction == "down":
                aim += int(amount)
            if instruction == "up":
                aim -= int(amount)

    logger.info(f"Day {day} part {part} result: {pos}-{depth}-{aim} => {pos * depth}")


if __name__ == "__main__":
    main()
