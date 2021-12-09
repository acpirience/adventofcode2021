from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def main():
    """
    https://adventofcode.com/2021/day/9
    """
    day = "9"
    part = "1"

    logger.info(f"Day {day} part {part}")

    heights = []
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            heights.append(str_array_to_int(line.rstrip()))

    logger.info(heights)
    dim_y = len(heights[0])
    dim_x = len(heights)
    logger.info(f"dim_x={dim_x} dim_y={dim_y}")

    result = 0
    for x in range(dim_x):
        for y in range(dim_y):
            lowest = True
            test = heights[x][y]
            if x > 0 and test >= heights[x - 1][y]:
                lowest = False
            if x < (dim_x - 1) and test >= heights[x + 1][y]:
                lowest = False
            if y > 0 and test >= heights[x][y - 1]:
                lowest = False
            if y < (dim_y - 1) and test >= heights[x][y + 1]:
                lowest = False

            if lowest:
                result += test + 1
                logger.info(f"{x}-{y} => {test}")

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
