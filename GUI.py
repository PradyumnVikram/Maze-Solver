__author__ = 'Pradyumn Vikram'


from PathFinder import Solver
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 144)
BLUE = (0, 0, 255)

WIDTH = 20
HEIGHT = 20
win_size = (255, 255)

pygame.display.set_caption('MAZE SOLVER')
win = pygame.display.set_mode(win_size)
MARGIN = 5


def redraw_window(screen, grid, solve):
    win.fill(BLACK)

    for row in range(10):
        for col in range(10):
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
    if maze[row][col] == 1:
        maze[row][col] = 0
    elif maze[row][col] == 0:
        maze[row][col] = 1


def main():
    maze = [[1 for _ in range(10)] for _ in range(10)]
    clock = pygame.time.Clock()
    run = True
    solve = False
    while run:
        clock.tick(60)
        redraw_window(win, maze, solve)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if not solve:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    get_col_row(maze)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                solve = True
                engine = Solver(10, maze)

                sol = engine.solve_maze()
                if sol:
                    maze = sol
                else:
                    print('Not found')
                    solve = False
    pygame.quit()


main()
