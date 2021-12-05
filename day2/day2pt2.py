from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/2#part2
    """
    day = "2"
    part = "2"

    logger.info(f"Day {day} part {part}")
    # load input
    with open("day" + day + "\\day" + day + "exampleinput.txt", "r") as inputFile:
        pass

    logger.info(f"Day {day} part {part} result: ")


if __name__ == "__main__":
    main()
