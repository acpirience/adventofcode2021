from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def main():
    """
    https://adventofcode.com/2021/day/6#part2
    """
    day = "6"
    part = "2"

    logger.info(f"Day {day} part {part}")

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        state = str_array_to_int(inputFile.readline().split(","))

    # naive solution used in part 1 can't work anymore because it's too slow

    # in fish_timers we store the number of fishes with timer 0,1,2,3,4,5,6,7 and 8
    # each day fish_timers decrease by one so each number of fish goes to the cell before
    # except for 0 that is added to the 6th timer and moved to 8th
    fish_timers = [0] * 9
    # load fish_timers
    for cell in state:
        fish_timers[cell] += 1

    logger.info(f"initial state: {fish_timers}")

    for day in range(1, 257):
        tmp_timers = [0] * 9
        for i in range(1, 9):
            tmp_timers[i - 1] = fish_timers[i]
        tmp_timers[8] = fish_timers[0]
        tmp_timers[6] += fish_timers[0]

        fish_timers = tmp_timers
        logger.info(f"After {day} days: {fish_timers}")

    logger.info(f"Day {day} part {part} result: {sum(fish_timers)}")


if __name__ == "__main__":
    main()
