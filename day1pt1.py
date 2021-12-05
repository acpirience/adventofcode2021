from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/1
    """
    day = "1"
    part = "1"

    logger.info("Day " + day)
    # load input
    increased = 0
    with open("day" + day + "input.txt", "r") as inputFile:
        prev_line = int(inputFile.readline())

        for line in inputFile.readlines():
            line = int(line)
            if line > prev_line:
                increased += 1

            prev_line = line

    logger.info(f"Day {day} part {part} result: " + str(increased))


if __name__ == "__main__":
    main()
