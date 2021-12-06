from loguru import logger
from bingo import Bingo


def main():
    """
    https://adventofcode.com/2021/day/4
    """
    day = "4"
    part = "1"

    logger.info(f"Day {day} part {part}")

    nb_cards = 0
    tmp_card = []
    card_list = []
    # load input
    with open("day" + day + "\\day" + day + "input.txt", "r") as inputFile:
        drawn_numbers = inputFile.readline().rstrip().split(",")
        lines = inputFile.readlines()
        for line in lines:
            line = line.rstrip()
            if line == "":  # Start new card, end previous
                if nb_cards != 0:
                    card_list.append(Bingo(tmp_card))
                    tmp_card = []
                nb_cards += 1
            else:
                tmp_card.append(line.rstrip().split())

        # store last card
        card_list.append(Bingo(tmp_card))

    is_bingo = False
    winner = None
    number_winner = None
    for number in drawn_numbers:
        logger.info(f"checking for number {number}")
        for card in card_list:
            card.mark(number)
            if card.check_for_line():
                logger.info(f"Bingo !")
                is_bingo = True
                winner = card
                number_winner = number
                break
        if is_bingo:
            break

    logger.info(f"\n{winner}")

    logger.info(
        f"Day {day} part {part} result: {winner.calculate_score(number_winner)}"
    )


if __name__ == "__main__":
    main()
