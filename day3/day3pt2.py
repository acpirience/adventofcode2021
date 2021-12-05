from loguru import logger


def get_lines_with_criteria(curr_lines, bit, param):
    ret_lines = []
    accum = 0
    thres = len(curr_lines) / 2

    for i in range(len(curr_lines)):
        accum += int(curr_lines[i][bit])

    if param == "most":
        if accum >= thres:
            ret_lines = [x for x in curr_lines if x[bit] == "1"]
        else:
            ret_lines = [x for x in curr_lines if x[bit] == "0"]
    else:
        if accum < thres:
            ret_lines = [x for x in curr_lines if x[bit] == "1"]
        else:
            ret_lines = [x for x in curr_lines if x[bit] == "0"]

    return ret_lines


def main():
    """
    https://adventofcode.com/2021/day/3#part2
    """
    day = "3"
    part = "2"

    logger.info(f"Day {day} part {part}")

    tot_lines = []
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            tot_lines.append(line.rstrip())

    curr_lines = tot_lines
    for bit in range(len(tot_lines[0])):
        curr_lines = get_lines_with_criteria(curr_lines, bit, "most")
        if len(curr_lines) == 1:
            break

    oxygen_generator_rating = int("".join(curr_lines), base=2)

    curr_lines = tot_lines
    for bit in range(len(tot_lines[0])):
        curr_lines = get_lines_with_criteria(curr_lines, bit, "least")
        if len(curr_lines) == 1:
            break

    c02_scrubber_rating = int("".join(curr_lines), base=2)

    logger.info(
        f"Day {day} part {part} result: {oxygen_generator_rating}-{c02_scrubber_rating}-{oxygen_generator_rating * c02_scrubber_rating}"
    )


if __name__ == "__main__":
    main()
