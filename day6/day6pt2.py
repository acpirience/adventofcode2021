from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/6#part2
    """
    day = "6"
    part = "2"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "exampleinput.txt", "r") as inputFile:
        for line in inputFile.readlines():
            pass

    logger.info(f"Day {day} part {part} result:")


if __name__ == "__main__":
    main()
