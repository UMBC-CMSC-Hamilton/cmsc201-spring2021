import random


class ConwayGameofLife:
    # this is where you can put constants
    DEAD = ' '
    ALIVE = 'X'

    def __init__(self, board_x, board_y):
        # False if the board is dead at that position
        # True if it is "alive"
        self.the_board = []
        for i in range(board_x):
            row = []
            for j in range(board_y):
                row.append(self.DEAD)
            self.the_board.append(row)

    def populate_randomly(self, prob):
        """
        :param prob: 0 < prob < 1 is the probability that we will fill in a space with a live entity,
        the rest are set to dead

        sets self.the_board
        return nothing
        """
        for i in range(len(self.the_board)):
            for j in range(len(self.the_board[0])):
                if random.random() < prob:
                    self.the_board[i][j] = self.ALIVE

    def display_board(self):
        """
            displays the board contained in self.the_board
        """
        for i in range(len(self.the_board)):
            print(' '.join(self.the_board[i]))

    def step(self):
        """
            Remember the rules, if at any space the number of adjacents is 0, 1, or bigger than 3 -> dead
            else alive.
        """
        new_board = []
        for i in range(len(self.the_board)):
            new_row = []
            for j in range(len(self.the_board[0])):
                new_row.append(self.set_dead_or_alive(i, j))
            new_board.append(new_row)
        self.the_board = new_board

    def set_dead_or_alive(self, x, y):
        num_adjacent = 0
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                # we don't want to go overboard
                if 0 <= x + x_offset < len(self.the_board) and 0 <= y + y_offset < len(self.the_board[0]):
                    # if x_offset and y_offset are both 0, then we're not looking at an adjacent square
                    # we would have been looking at THE SQUARE ITSELF so check for that too
                    if self.ALIVE == self.the_board[x + x_offset][y + y_offset]:
                        if x_offset != 0 or y_offset != 0:
                            num_adjacent += 1

        if num_adjacent == 2 and self.the_board[x][y] == self.ALIVE:
            return self.ALIVE
        elif num_adjacent == 3:
            return self.ALIVE
        else:
            return self.DEAD


if __name__ == '__main__':
    cgl = ConwayGameofLife(5, 5)
    cgl.populate_randomly(float(input('Enter the probability for filling: ')))
    cgl.display_board()
    s = input('Continue or Quit')
    while s.lower() != 'quit':
        cgl.step()
        cgl.display_board()
        s = input('Continue or Quit')
