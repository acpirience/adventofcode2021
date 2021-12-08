from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/8
    """
    day = "8"
    part = "1"

    logger.info(f"Day {day} part {part}")

    inputs = []
    outputs = []
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            tmp_in, tmp_out = line.split("|")
            inputs.append(tmp_in.split())
            outputs.append(tmp_out.split())

    nb_digits = [0] * 8
    for line in outputs:
        for cell in line:
            nb_digits[len(cell)] += 1

    # 0 uses 6 segments
    # 1 uses 2 segments ***
    # 2 uses 5 segments
    # 3 uses 5 segments
    # 4 uses 4 segments ***
    # 5 uses 5 segments
    # 6 uses 6 segments
    # 7 uses 3 segments ***
    # 8 uses 7 segments ***
    # 9 uses 6 segments

    result = nb_digits[2] + nb_digits[4] + nb_digits[3] + nb_digits[7]

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
