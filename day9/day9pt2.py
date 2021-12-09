from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def xy_to_str(xy):
    return f"{xy[0]}-{xy[1]}"


def check_for_nines(xy, heights):
    not_nines = []
    dim_y = len(heights[0])
    dim_x = len(heights)
    x = xy[0]
    y = xy[1]

    if x > 0 and heights[x - 1][y] < 9:
        not_nines.append([x - 1, y])
    if x < (dim_x - 1) and heights[x + 1][y] < 9:
        not_nines.append([x + 1, y])
    if y > 0 and heights[x][y - 1] < 9:
        not_nines.append([x, y - 1])
    if y < (dim_y - 1) and heights[x][y + 1] < 9:
        not_nines.append([x, y + 1])

    return not_nines


def main():
    """
    https://adventofcode.com/2021/day/9#part2
    """
    day = "9"
    part = "2"

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

    lowest_locations = []
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
                lowest_locations.append([x, y])

    result = []
    logger.info(f"lowest=>{lowest_locations}")
    for loc in lowest_locations:
        logger.info(f"check for {loc}")
        basin = [loc]
        allready_checked = []
        for xy in basin:
            if not xy_to_str(xy) in allready_checked:
                basin.extend(check_for_nines(xy, heights))
                allready_checked.append(xy_to_str(xy))

        mybasin = [xy_to_str(xy) for xy in basin]
        mybasin = list(dict.fromkeys(mybasin))
        logger.info(f"loc {loc} => basin {mybasin} => len {len(mybasin)}")
        result.append(len(mybasin))

    result.sort(reverse=True)
    final_result = 1
    for i in range(3):
        final_result *= result[i]

    logger.info(f"Day {day} part {part} result: {final_result}")


if __name__ == "__main__":
    main()
