import random

GRID_SIZE = 4


### Grid Functions: Initialize the grid, print the grid, and add random tiles.
def initialize_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid

def add_random_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2

def print_grid(grid):
    for row in grid:
        print("\t".join(str(cell) if cell != 0 else "." for cell in row))
    print()


### Helper Functions: compress, merge, transpose, and reverse rows and columns.
def compress(grid):
    new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for i in range(GRID_SIZE):
        pos = 0
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid

def merge(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    return grid

def reverse(grid):
    new_grid = [row[::-1] for row in grid]
    return new_grid

def transpose(grid):
    new_grid = [[grid[j][i] for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    return new_grid


## Movement Functions: Functions for each direction (move_up, move_down, move_left, move_right)
def move_left(grid):
    grid = compress(grid)
    grid = merge(grid)
    grid = compress(grid)
    return grid

def move_right(grid):
    grid = reverse(grid)
    grid = move_left(grid)
    grid = reverse(grid)
    return grid

def move_up(grid):
    grid = transpose(grid)
    grid = move_left(grid)
    grid = transpose(grid)
    return grid

def move_down(grid):
    grid = transpose(grid)
    grid = move_right(grid)
    grid = transpose(grid)
    return grid


### Game Status Functions: Functions to check if the game is won or if moves are still possible.
def is_game_won(grid):
    for row in grid:
        if 2048 in row:
            return True
    return False

def is_move_possible(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return True
            if i < GRID_SIZE - 1 and grid[i][j] == grid[i + 1][j]:
                return True
            if j < GRID_SIZE - 1 and grid[i][j] == grid[i][j + 1]:
                return True
    return False
