import pygame as pg
from solver import Solver
import numpy as np

if __name__ == '__main__':

    top_left_corner_x = 100
    top_left_corner_y = 100
    gap = 5
    rect_width = 50
    rect_height = 50
    
    pg.init()
    screen = pg.display.set_mode((2 * 100 + 9 * rect_width + 8 * gap, 2 * 100 + 9 * rect_height + 8 * gap))
    pg.display.set_caption('SudokuSolver')
    clock = pg.time.Clock()
    font = pg.font.Font('freesansbold.ttf', 24)
    runnning = True
    solving = False

    sudoku_cells = []
    selected_cell = 0

    for row in range(9):
        for col in range(9):
            sudoku_cells.append({
                'width': rect_width, 
                'height': rect_height,
                'top_left_y': top_left_corner_y + row * (gap + rect_height),
                'top_left_x': top_left_corner_x + col * (gap + rect_width),
                'text': '0',
                })

    while runnning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    selected_cell += 9
                elif event.key == pg.K_RIGHT:
                    selected_cell += 1
                elif event.key == pg.K_LEFT:
                    selected_cell += -1
                elif event.key == pg.K_UP:
                    selected_cell += -9
                elif event.unicode.isnumeric():
                    sudoku_cells[selected_cell]['text'] = event.unicode
                elif event.key == pg.K_b:
                    print('initiating solve')
                    board = [int(cell['text']) for cell in sudoku_cells]
                    solver = Solver(board)
                    solving = True

                selected_cell %= 81

        screen.fill('black')

        '''
        for _board in solver.solve():
                        for index, cell_value in enumerate(_board):
                            sudoku_cells[index]['text'] = f'{cell_value}'
                        pg.display.flip()
                        if len(np.where(_board==0)[0])==0:
                            break
                        '''
        if solving:
            for _board in solver.solve():
                for index, cell_value in enumerate(_board):
                    sudoku_cells[index]['text'] = f'{cell_value}'
                
                for index, cell in enumerate(sudoku_cells):
                    pg.draw.rect(screen, 'white' if selected_cell == index else 'gray', pg.Rect(cell['top_left_x'], cell['top_left_y'], rect_width, rect_height))
                    text = font.render(cell['text'], True, 'black')
                    textRect = text.get_rect()
                    textRect.center = (cell['top_left_x'] + rect_width//2, cell['top_left_y'] + rect_height//2)
                    screen.blit(text, textRect)

                pg.display.flip()
                
                if len(np.where(_board==0)[0])==0:
                    break

        for index, cell in enumerate(sudoku_cells):
            pg.draw.rect(screen, 'white' if selected_cell == index else 'gray', pg.Rect(cell['top_left_x'], cell['top_left_y'], rect_width, rect_height))
            text = font.render(cell['text'], True, 'black')
            textRect = text.get_rect()
            textRect.center = (cell['top_left_x'] + rect_width//2, cell['top_left_y'] + rect_height//2)
            screen.blit(text, textRect)

        pg.display.flip()

        clock.tick(60)

pg.quit()