from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/5
    """
    day = "5"
    part = "1"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        pass

    logger.info(f"Day {day} part {part} result: ")


if __name__ == "__main__":
    main()
