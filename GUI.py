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

pygame.display.set_caption('Maze Solver')
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
            elif grid[row][col] == 4:
                color = (0,220,255)
            elif grid[row][col] == 3:
                color = (0,220,255)
            elif grid[row][col] == 5:
                color = (0,255,0)

            pygame.draw.rect(win, color, [(MARGIN + WIDTH)*col + MARGIN,
                                          (MARGIN + HEIGHT)*row + MARGIN,
                                          WIDTH,
                                          HEIGHT])
    pygame.display.flip()
    pygame.display.update()


def get_col_row(maze, declared, start):
    pos = pygame.mouse.get_pos()
    col = pos[0]//(WIDTH+MARGIN)
    row = pos[1]//(HEIGHT+MARGIN)
    try:
        if declared:
            if maze[row][col] == 1:
                maze[row][col] = 0
        else:
            if start % 2 != 0:
                maze[row][col] = 3
            elif start % 2 == 0:
                maze[row][col] = 4
        return [row, col]
        
    except IndexError as e:
        pass


def main():
    maze = PathFinder.new_board(n_size)
    clock = pygame.time.Clock()
    run = True
    solve = False
    declared = False
    start = 1
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
                if pygame.mouse.get_pressed()[0] and declared:
                    try:
                        get_col_row(maze, declared, start)
                    except AttributeError:
                        pass
                elif not declared:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start % 2 != 0:
                            start_pos = get_col_row(maze, declared, start)
                            start += 1
                        else:
                            
                            final = get_col_row(maze, declared, start)
                            declared = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                solve = True
                engine = Solver(n_size, maze)
                maze[start_pos[0]][start_pos[1]] = 1
                sol = engine.solve_maze(final, start_pos)
                if sol:
                    maze = sol
                    c = 0
                    for x in maze:
                        for val in x:
                            if val == 5:
                                c+=1
                    print(c, ' cells visited before achieveing solution path')
                else:
                    print('Not found')
                    solve = False
            elif keys[pygame.K_r]:
                maze = PathFinder.new_board(n_size)
                declared = False
                start = 1
                solve = False
    pygame.quit()


main()
