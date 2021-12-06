from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def main():
    """
    https://adventofcode.com/2021/day/6
    """
    day = "6"
    part = "1"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        state = str_array_to_int(inputFile.readline().split(","))

    for day in range(1, 81):
        new_fishes = 0
        for i in range(len(state)):
            if state[i] > 0:
                state[i] -= 1
            else:
                state[i] = 6
                new_fishes += 1
        if new_fishes > 0:

            state.extend([8] * new_fishes)

        logger.info(f"After {day} day: {state}")

    logger.info(f"Day {day} part {part} result: {len(state)}")


if __name__ == "__main__":
    main()
