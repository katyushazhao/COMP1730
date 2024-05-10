## COMP1730/6730 Homework 5

# Your ANU ID: u7650690
# Your NAME: Aria Zhao
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]

## You should implement the functions `count_live_neighbours` and `generate_next_board`
## below. You can define new function(s) if it helps you decompose the problem
## into smaller problems.

## Note this is the version of game_of_life that uses a lists of lists and NOT NumPy.

def count_live_neighbours(board, row, column):
    '''returns the number of live neighbours of a cell'''
    live = 0
    live += is_alive(board, row-1, column-1)
    live += is_alive(board, row, column-1)
    live += is_alive(board, row+1, column-1)
    live += is_alive(board, row-1, column)
    live += is_alive(board, row+1, column)
    live += is_alive(board, row-1, column+1)
    live += is_alive(board, row, column+1)
    live += is_alive(board, row+1, column+1)
    return live


def is_alive(board, row, column):
    '''Returns 1 if the given cell is alive.'''
    if on_board(board, row, column) == True:
        return board[row][column]
    else:
        return 0

def boardsize(board):
    '''Returns an array with the number of rows and columns in the board.'''
    rows = len(board)
    cols = len(board[0])
    return [rows, cols]

def on_board(board, row, column):
    '''Checks if a given point is on the board'''
    if row >= 0 and row < boardsize(board)[0] and column >= 0 and column < boardsize(board)[1]:
        return True
    else:
        return False

def generate_next_board(board):
    '''Given the current board, generates the next board'''
    newboard = [[0]*boardsize(board)[1]]*boardsize(board)[0]
    print(board)
    print("\n")
    row = 0
    while row < boardsize(board)[0]:
        column = 0
        while column < boardsize(board)[1]:
            if board[row][column] == 1:
                if count_live_neighbours(board,row,column) == 0 or count_live_neighbours(board,row,column) == 1:
                    newboard[row][column] = 0
                elif count_live_neighbours(board,row,column) == 2 or count_live_neighbours(board,row,column) == 3:
                    newboard[row][column] = 1
                else:
                    newboard[row][column] = 0
            if board[row][column] == 0:
                if count_live_neighbours(board,row,column) == 3:
                    newboard[row][column] = 1
            print(newboard)
            print(str(row)+str(column))
            column += 1
        row += 1
    return newboard
                



################################################################################
#                  VISUALISATION AND EXAMPLE BOARDS
################################################################################

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def draw_board(board):
    """Draws the given board in a new figure. The figure and lines plot are also returned."""
    fig  = plt.figure()
    plot = plt.imshow(board)
    return fig, plot

def evolve_life(initial_generation, number_steps):
    """
    Show the evolution of the board as an animation.

    The function will return a handle to the animation object.
    This handle *must* be assigned to a variable otherwise the animation may freeze.
    For example:
        `anim = evolve_life(my_board, number_steps_wanted)`
    If you only do the following, the animation may freeze:
        `evolve_life(my_board, number_steps_wanted)`

    Parameters
    ----------
    initial_generation : list of list
        The initial/starting board
    number_steps : int
        How many times the board is to be evolved/updated.
        Should be greater than 0.

    Returns
    -------
    anim : FuncAnimation instance
        Animation object handle.
        **Must be assigned to a variable or animation may freeze.**

    """
    def animate(i):
        plot.set_data(generations[i])
        return [plot]
    fig, plot = draw_board(initial_generation)
    generations = [initial_generation]
    for i in range(1, number_steps):
        generations.append(generate_next_board(generations[i-1]))
    anim = FuncAnimation(fig, animate, frames=number_steps, interval=100, blit=True)
    plt.show()
    return anim

def evolve_life_beacon(steps):
    """Show the animation of the Beacon board (a period 2 oscillator) being evolved the specified number of steps."""
    beacon = [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]]
    return evolve_life(beacon, steps)

def evolve_life_glider_gun(steps):
    """Show the animation of the Glider board being evolved the specified number of steps."""
    glider_gun_inner = \
        [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    glider_gun = np.zeros((100, 100))
    glider_gun[3:12,3:39] = glider_gun_inner
    glider_gun = glider_gun.tolist()
    return evolve_life(glider_gun, steps)

def evolve_life_line(steps):
    """Show the animation of the Line board (a simple board) being evolved the specified number of steps."""
    line_inner = [[1,1,1,1,1,1,1,1,1,1]]
    line = np.zeros((50, 50))
    line[25:26,20:30] = line_inner
    line = line.tolist()
    return evolve_life(line, steps)

def evolve_life_box(steps):
    """Show the animation of the Box board (another simple board) being evolved the specified number of steps."""
    box_inner = \
        [[1,0,1,0,1],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [1,0,1,0,1]]
    box = np.zeros((50, 50))
    box[23:28,23:28] = box_inner
    box = box.tolist()
    return evolve_life(box, steps)


## Un-comment one or more of the lines below to show the life of a board.
# animation1 = evolve_life_beacon(10)
# animation2 = evolve_life_glider_gun(1000)
# animation3 = evolve_life_line(1000)
# animation4 = evolve_life_box(1000)


################################################################################
#               DO NOT MODIFY ANYTHING BELOW THIS POINT
################################################################################

def test_count_live_neighbours():
    """
    Run tests for the `count_live_neighbours` function.

    If all tests pass you will just see "all count_live_neighbours tests passed".
    If any test fails there will be an error message.

    **NOTE:**
        The tests we provide are intentionally not comprehensive and only cover a few of the simplest cases.
        Passing all the tests here does not automatically mean that your code is completely correct.
        Code that does not pass the basic tests included here will get 0 for functionality.

    You are expected to rerun this function before submitting.
    Carelessness and other similar excuses will **NOT** be accepted.
    """
    board = [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]]
    assert count_live_neighbours(board,0,0) == 1
    assert count_live_neighbours(board,1,1) == 3
    assert count_live_neighbours(board,2,2) == 4
    assert count_live_neighbours(board,3,5) == 2
    assert count_live_neighbours(board,5,3) == 2
    print("all count_live_neighbours tests passed")

def test_generate_next_board():
    """
    Run tests for the `generate_next_board` function.

    If all tests pass you will just see "all generate_next_board tests passed".
    If any test fails there will be an error message.

    **NOTE:**
        The tests we provide are intentionally not comprehensive and only cover a few of the simplest cases.
        Passing all the tests here does not automatically mean that your code is completely correct.
        Code that does not pass the basic tests included here will get 0 for functionality.

    You are expected to rerun this function before submitting.
    Carelessness and other similar excuses will **NOT** be accepted.
    """
    boards = [([[0,0,0],[0,0,0],[0,0,0]],
               [[0,0,0],[0,0,0],[0,0,0]]),

              ([[1,1,1],[1,1,1],[1,1,1]],
               [[1,0,1],[0,0,0],[1,0,1]]),

              ([[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,0,0,0,0],
                [0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]],
               [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],
                [0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]])]
    for board, next_board in boards:
        next_computed = generate_next_board(board)
        assert next_computed == next_board
    print("all generate_next_board tests passed")
