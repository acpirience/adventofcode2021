from loguru import logger


def main():
    """
    https://adventofcode.com/2021/day/3
    """
    day = "3"
    part = "1"

    logger.info(f"Day {day} part {part}")

    accum = []
    tot = 0
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            line = str(line.rstrip())
            tot += 1

            if not accum:
                accum = [int(line[x]) for x in range(len(line))]
            else:
                for bit in range(len(line)):
                    accum[bit] = accum[bit] + int(line[bit])

    thresh = tot // 2
    gamma = "".join(["1" if x > thresh else "0" for x in accum])
    epsilon = "".join(["0" if x > thresh else "1" for x in accum])

    gamma_rate = int(gamma, base=2)
    epsilon_rate = int(epsilon, base=2)

    logger.info(
        f"Day {day} part {part} result: {gamma_rate}-{epsilon_rate} => {gamma_rate * epsilon_rate}"
    )


if __name__ == "__main__":
    main()
