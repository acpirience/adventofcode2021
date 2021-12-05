from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/1#part2
    """
    day = "1"
    part = "2"

    logger.info(f"Day {day} part {part}")
    # load input
    increased = 0
    with open("day" + day + "input.txt", "r") as inputFile:
        lines = inputFile.readlines()
        lines = [int(line) for line in lines]
        max_lines = len(lines)
        prev_window = sum(lines[0:3])

        for i in range(1, max_lines - 2):
            window = sum(lines[i : i + 3])
            if window > prev_window:
                increased += 1

            prev_window = window

    logger.info(f"Day {day} part {part} result: {increased}")


if __name__ == "__main__":
    main()
