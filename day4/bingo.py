class Bingo:
    """
    Handles bingo cards
    """

    def __init__(self, numbers):
        self.cells = []
        for line in numbers:
            self.cells.append(
                [
                    Cell(line[0]),
                    Cell(line[1]),
                    Cell(line[2]),
                    Cell(line[3]),
                    Cell(line[4]),
                ]
            )
        self.has_won = False

    def __repr__(self):
        tmp_str = ""
        for line in self.cells:
            tmp_str += f"{line[0]} {line[1]} {line[2]} {line[3]} {line[4]} \n"
        return tmp_str

    def mark(self, number):
        for line in self.cells:
            for cell in line:
                if cell.number == number:
                    cell.drawn = True

    def check_for_line(self):
        for i in range(5):
            if (
                self.cells[i][0].drawn
                and self.cells[i][1].drawn
                and self.cells[i][2].drawn
                and self.cells[i][3].drawn
                and self.cells[i][4].drawn
            ):
                return True
            if (
                self.cells[0][i].drawn
                and self.cells[1][i].drawn
                and self.cells[2][i].drawn
                and self.cells[3][i].drawn
                and self.cells[4][i].drawn
            ):
                return True

    def calculate_Score(self, number):
        unmarked = 0
        for line in self.cells:
            for cell in line:
                if not cell.drawn:
                    unmarked += int(cell.number)
        return unmarked * int(number)


class Cell:
    """
    cell object, a card uis made of 5*5 cells
    """

    def __init__(self, number):
        self.number = number
        self.drawn = False

    def __repr__(self):
        tmp_str = ""
        if self.drawn:
            tmp_str += "*"
        else:
            tmp_str += " "
        return f"{tmp_str}{self.number: >2}"
