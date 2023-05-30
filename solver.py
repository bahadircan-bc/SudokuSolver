import numpy as np
import time

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
    
    def recursive_solve(self, board):
        _board = np.copy(board)
        # time.sleep(0.01)
        zero_slots = np.where(_board==0)
        if len(zero_slots[0]) == 0:
            print(np.reshape(_board, (9, 9)))
            print('solved...')
            self.solved_board = _board
            return True
        slot = zero_slots[0][0]
        for value in range(1,10):
            if self.is_valid_horizontal_and_vertical(board=_board, index=slot, value=value) and self.is_valid_in_square(board=_board, index=slot, value=value):
                _board[slot] = value
                print(f'{np.reshape(_board, (9, 9))}{self.up_one_line * 9}')
                if self.recursive_solve(board=_board):
                    return True
        return False

    def solve(self):
        if not self.recursive_solve(self.board):
            print('impossible board')
        else:
            return self.solved_board


if __name__ == '__main__':
    # board is going to be a flattened array with 81 elements
    # row and col numbers is 1 indexed to increase readability
    random_board = np.array([
        [0, 0, 4, 0, 3, 0, 0, 6, 7],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [8, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 4, 0, 0],
        [0, 0, 5, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 3, 0, 0, 0, 5, 9],
        [0, 0, 6, 0, 7, 0, 0, 3, 5],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 4, 0, 0, 0, 6, 0, 0, 0]
 ])

    solver = Solver(board=random_board)
    print(solver.solve())