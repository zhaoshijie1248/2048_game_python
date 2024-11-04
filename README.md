# 2048 Game in Python

This is a simple command-line implementation of the popular 2048 game. The objective of the game is to slide numbered tiles on a 4x4 grid and combine them to reach the 2048 tile. This project is built in Python with a focus on modularity and simplicity, and it provides an educational exercise in working with matrices, user input handling, and game logic.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)

## Features
- A 4x4 grid where tiles slide in four directions (up, down, left, right).
- Automatic merging of tiles when two tiles with the same value collide.
- Randomly generated "2" tiles after each move.
- Win condition when the player reaches 2048.
- Lose condition when no more moves are possible.
- Input validation and error handling for smoother gameplay.

## Requirements
- Python 3.x
- No additional libraries are needed; the code only uses standard Python libraries.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/zhaoshijie1248/2048_game_python.git
    ```
2. Navigate to the project directory:
    ```bash
    cd 2048_game_python
    ```

## How to Play
1. Run the `main.py` file to start the game:
    ```bash
    python main.py
    ```
2. Use the following keys to move tiles:
   - **w**: Move Up
   - **a**: Move Left
   - **s**: Move Down
   - **d**: Move Right

3. After each move, a new tile with the number 2 will appear in an empty spot on the grid.
4. The game ends when you create a tile with the number 2048 (win) or when there are no possible moves left (lose).

## Project Structure

- `main.py`: The main script that runs the game, handles user input, and controls the game flow.
- `game_functions.py`: Contains helper functions for grid initialization, movement, merging tiles, and game status checks.

### Detailed Explanation of Files

1. **`main.py`**:
    - Manages the game loop and checks for win/lose conditions.
    - Accepts user input for moves and calls corresponding functions.
    - Imports functions from `game_functions.py` to handle grid updates and display.

2. **`game_functions.py`**:
    - `initialize_grid`: Sets up the initial 4x4 grid and adds two random tiles.
    - `add_random_tile`: Adds a "2" tile in a random empty cell.
    - `move_left`, `move_right`, `move_up`, `move_down`: Functions to handle movement in each direction.
    - `is_game_won`: Checks if a 2048 tile is present, signifying a win.
    - `is_move_possible`: Checks if there are possible moves left.
