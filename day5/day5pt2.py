from loguru import logger


def str_array_to_int(pt):
    return [int(x) for x in pt]


def is_horizontal(pt1, pt2):
    return pt1[1] == pt2[1]


def is_vertical(pt1, pt2):
    return pt1[0] == pt2[0]


def is_45_degrees(pt1, pt2):
    return abs(pt1[0] - pt2[0]) == abs(pt1[1] - pt2[1])


def show_map(table):
    tmp = "\n"
    for line in table:
        for cell in line:
            if cell == 0:
                tmp += "."
            else:
                tmp += str(cell)
        tmp += "\n"
    return tmp


def main():
    """
    https://adventofcode.com/2021/day/5#part2
    """
    day = "5"
    part = "2"

    logger.info(f"Day {day} part {part}")

    # Ocean_floor is a 1000 * 1000 array
    ocean_floor = [[0] * 1000 for _ in range(1000)]

    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            tmp_from, tmp_to = line.split(" -> ")
            pt_from = str_array_to_int(tmp_from.rstrip().split(","))
            pt_to = str_array_to_int(tmp_to.rstrip().split(","))

            logger.info(f"{pt_from} -> {pt_to}")

            if is_horizontal(pt_from, pt_to):
                for x in range(
                    min(pt_from[0], pt_to[0]), max(pt_from[0], pt_to[0]) + 1
                ):
                    ocean_floor[pt_from[1]][x] += 1

            if is_vertical(pt_from, pt_to):
                for y in range(
                    min(pt_from[1], pt_to[1]), max(pt_from[1], pt_to[1]) + 1
                ):
                    ocean_floor[y][pt_from[0]] += 1

            if is_45_degrees(pt_from, pt_to):
                sgn_x = (pt_to[0] - pt_from[0]) // abs(pt_to[0] - pt_from[0])
                sgn_y = (pt_to[1] - pt_from[1]) // abs(pt_to[1] - pt_from[1])

                for i in range(abs(pt_from[0] - pt_to[0]) + 1):
                    ocean_floor[pt_from[1] + i * sgn_y][pt_from[0] + i * sgn_x] += 1

    cnt = 0
    for line in ocean_floor:
        for cell in line:
            if cell >= 2:
                cnt += 1

    logger.info(f"Day {day} part {part} result: {cnt}")


if __name__ == "__main__":
    main()
