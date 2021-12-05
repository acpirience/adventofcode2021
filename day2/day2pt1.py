from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/2
    """
    day = "2"
    part = "1"

    logger.info(f"Day {day} part {part}")

    pos = 0
    depth = 0
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            instruction, amount = line.split(" ")
            if instruction == "forward":
                pos += int(amount)
            if instruction == "down":
                depth += int(amount)
            if instruction == "up":
                depth -= int(amount)

    logger.info(f"Day {day} part {part} result: {pos}-{depth} => {pos * depth}")


if __name__ == "__main__":
    main()
