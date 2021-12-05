from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/3#part2
    """
    day = "3"
    part = "2"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "exampleinput.txt", "r") as inputFile:
        for line in inputFile.readlines():
            logger.info(line.rstrip())

    logger.info(f"Day {day} part {part} result: ")


if __name__ == "__main__":
    main()
