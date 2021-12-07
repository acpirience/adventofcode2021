from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def compute_fuel(x, y):
    ret = 0
    for i in range(1, abs(x - y) + 1):
        ret += i
    return ret


def main():
    """
    https://adventofcode.com/2021/day/7#part2
    """
    day = "7"
    part = "2"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        positions = str_array_to_int(inputFile.readline().split(","))

    min_fuel = None
    best_position = None
    for x in range(min(positions), max(positions) + 1):
        curr_fuel = 0
        for position in positions:
            curr_fuel += compute_fuel(position, x)
        if min_fuel is None or curr_fuel < min_fuel:
            min_fuel = curr_fuel
            best_position = x

        logger.info(
            f"pos {x} - fuel:{curr_fuel} - min fuel:{min_fuel} - best pos:{best_position}"
        )

    logger.info(f"Day {day} part {part} result: {min_fuel}")


if __name__ == "__main__":
    main()
