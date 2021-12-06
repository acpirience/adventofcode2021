from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def main():
    """
    https://adventofcode.com/2021/day/7
    """
    day = "7"
    part = "1"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        pass

    logger.info(f"Day {day} part {part} result: ")


if __name__ == "__main__":
    main()
