import numpy as np
import time

with open('solution.txt', 'w') as file:
    file.write('\n')

class Solver:
    up_one_line = '\033[F'

    def __init__(self, board) -> None:
        self.board = np.array(board).flatten()

    def is_valid_horizontal_and_vertical(self, board, index, value) -> bool:
        row = int(index / 9)
        col = index % 9
        _board = np.reshape(board, (9, 9))
        _board[row, col] = 0
        # scans in the same row
        for val in _board[row][::]:
            if val == value:
                return False
        # scans in the same column
        for val in _board[::, col]:
            if val == value:
                return False
        return True

    def is_valid_in_square(self, board, index, value) -> bool:
        row = int(index / 9)
        col = index % 9
        _board = np.reshape(board, (9, 9))
        _board[row, col] = 0
        nth_box_in_row = int(row / 3)
        # nth_row_in_box = (row) % 3
        nth_box_in_col = int(col / 3)
        # nth_col_in_box = (col) % 3
        box_row_start = nth_box_in_row*3
        box_col_start = nth_box_in_col*3
        # creates the box containing given slot
        box = _board[box_row_start:box_row_start+3, box_col_start:box_col_start+3].flatten()
        # scans the box
        for val in box:
            if val == value:
                return False
        return True
    
    def solve(self):
        _board = np.copy(self.board)
        # time.sleep(0.01)
        yield _board
        for next_board in self.solve():
            zero_slot = np.where(next_board==0)[0][0]
            for value in range(1,10):
                if self.is_valid_horizontal_and_vertical(board=next_board, index=zero_slot, value=value) and self.is_valid_in_square(board=next_board, index=zero_slot, value=value):
                    new_board = np.copy(next_board)
                    new_board[zero_slot] = value
                    yield new_board
         


if __name__ == '__main__':
    # board is going to be a flattened array with 81 elements
    # row and col numbers is 1 indexed to increase readability
    random_board = np.array([
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [1, 0, 3, 4, 0, 0, 0, 0, 5],
        [2, 0, 0, 0, 5, 0, 4, 0, 1],
        [3, 4, 0, 0, 0, 5, 0, 9, 0],
        [8, 0, 7, 0, 0, 0, 3, 0, 4],
        [0, 9, 0, 3, 0, 0, 0, 1, 7],
        [6, 0, 5, 0, 3, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 8, 7, 0, 2],
        [0, 0, 0, 1, 0, 0, 0, 0, 0]
 ])

    solver = Solver(board=random_board)
    for _board in solver.solve():
        print(_board)
        zeroes = np.where(_board==0)
        print(len(zeroes[0]))
        if len(zeroes[0]) == 0:
            break
    else:
        print('in else')
    print('im executed')
    # print(solver.solve())