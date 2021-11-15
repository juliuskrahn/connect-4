class Game:

    def __init__(self):
        self.board = [[0] * 6 for i in range(7)]  # [ columns ]
        self.player = 1

    def fill_column(self, c):
        if not 0 <= c < len(self.board):
            raise ValueError()
        for i in range(len(self.board[c]) - 1, -1, -1):  # walk reverse
            if self.board[c][i] == 0:
                self.board[c][i] = self.player
                break
        else:
            raise ValueError()
        self.player *= -1

    def evaluate(self):
        sections = str([
            *self.board,  # columns
            *[[column[r] for column in self.board] for r in range(len(self.board[0]))],  # rows
            *[[self.board[c][r] if r < len(self.board[0]) else 0 for r, c in enumerate(range(c, len(self.board)))] for c in range(len(self.board))],  # diagonals (column wise)
            *[[self.board[c][r] for c, r in enumerate(range(r, len(self.board[0])))] for r in range(len(self.board[0]))],  # diagonals (row wise)
        ])
        for player in [1, -1]:
            if str([player] * 4)[1:-1] in sections:
                return player  # winner
        if min([column[0] for column in self.board]) != 0:
            return 0  # draw


class Terminal:

    def __init__(self):
        self.game = Game()
        self.print_board()

    def start(self):
        while True:
            try:
                c = int(input(self.player_symbol(self.game.player) + ": "))
                self.game.fill_column(c)
                self.print_board()
                if winner := self.game.evaluate():
                    print("-- " + self.player_symbol(winner) + " won --")
                elif winner == 0:
                    print("-- Draw --")
                else:
                    continue
                self.game = Game()
                self.print_board()
            except ValueError:
                continue

    def print_board(self):
        string = ""
        for r in range(len(self.game.board[0])):
            string += "\n|"
            for c in range(len(self.game.board)):
                string += self.player_symbol(self.game.board[c][r]) + "|"
        print(string)

    def player_symbol(self, player):
        if player == 0:
            return "\033[34m*\033[0m"
        if player == 1:
            return "\033[92mO\033[0m"
        return "\033[91mO\033[0m"


if __name__ == '__main__':
    Terminal().start()
