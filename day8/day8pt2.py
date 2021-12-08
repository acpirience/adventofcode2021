from loguru import logger
import itertools


def main():
    """
    https://adventofcode.com/2021/day/8#part2
    """
    day = "8"
    part = "2"

    logger.info(f"Day {day} part {part}")

    inputs = []
    outputs = []
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        for line in inputFile.readlines():
            tmp_in, tmp_out = line.split("|")
            inputs.append(tmp_in.split())
            outputs.append(tmp_out.split())

    valid_digits = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]

    transco_digit = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    result = 0

    for i in range(len(inputs)):
        max_ok = 0
        for candidate in itertools.permutations(
            "abcdefg"
        ):  # try all permutations of abcdefg
            dico = dict(zip("abcdefg", candidate))

            ok_list = []
            nb_ok = 0
            for digit in inputs[i]:
                test = "".join(sorted([dico[x] for x in digit]))
                if test in valid_digits:
                    nb_ok += 1
                    ok_list.append(digit)

            if max_ok < nb_ok:
                max_ok = nb_ok

            if max_ok == 10:  # we found 10 correct digits
                logger.info(f"line {i} ok = {nb_ok}")
                res = ""
                for digit in outputs[
                    i
                ]:  # calculate result with correct transcodification
                    test = "".join(sorted([dico[x] for x in digit]))
                    res += transco_digit[test]
                res = int(res)
                result += res
                logger.info(f"res:{res} => sum:{result}")
                break

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
