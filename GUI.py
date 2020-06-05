__author__ = 'Pradyumn Vikram'


from PathFinder import Solver
import PathFinder
import pygame

pygame.init()
n_size = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 144)
BLUE = (0, 0, 255)

WIDTH = 6
HEIGHT = 6
win_size = (403, 403)

pygame.display.set_caption('MAZE SOLVER')
win = pygame.display.set_mode(win_size)
MARGIN = 2


def redraw_window(screen, grid, solve):
    win.fill(BLACK)

    for row in range(n_size):
        for col in range(n_size):
            color = WHITE
            if grid[row][col] == 0:
                color = PINK
            elif grid[row][col] == 1:
                color = WHITE
            elif grid[row][col] == 2:
                color = BLUE

            pygame.draw.rect(win, color, [(MARGIN + WIDTH)*col + MARGIN,
                                          (MARGIN + HEIGHT)*row + MARGIN,
                                          WIDTH,
                                          HEIGHT])
    pygame.display.flip()
    pygame.display.update()


def get_col_row(maze):
    pos = pygame.mouse.get_pos()
    col = pos[0]//(WIDTH+MARGIN)
    row = pos[1]//(HEIGHT+MARGIN)
    try:
        if maze[row][col] == 1:
            maze[row][col] = 0
    except IndexError as e:
        pass


def main():
    maze = PathFinder.new_board(n_size)
    clock = pygame.time.Clock()
    run = True
    solve = False
    while run:
        clock.tick(60)
        redraw_window(win, maze, solve)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                try:
                    run = False
                    pygame.quit()
                except Exception as e:
                    run = False
                    pygame.quit()
            if not solve:
                if pygame.mouse.get_pressed()[0]:
                    try:
                        get_col_row(maze)
                    except AttributeError:
                        pass

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                solve = True
                engine = Solver(n_size, maze)

                sol = engine.solve_maze()
                if sol:
                    maze = sol
                else:
                    print('Not found')
                    solve = False
            elif keys[pygame.K_r]:
                maze = PathFinder.new_board(n_size)
                solve = False
    pygame.quit()


main()
