import tkinter as tk
import random

# Game constants
GRID_SIZE = 4
CELL_SIZE = 100
FONT = ("Verdana", 20, "bold")
BACKGROUND_COLOR = "#92877d"
EMPTY_CELL_COLOR = "#9e948a"
CELL_COLORS = {
    0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
    256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}
TEXT_COLORS = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2"}

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.game_over = False
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.setup_ui()
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        self.frame.pack(pady=20)
        
        self.cells = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell_frame = tk.Frame(
                    self.frame, width=CELL_SIZE, height=CELL_SIZE
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_label = tk.Label(
                    cell_frame, text="", bg=EMPTY_CELL_COLOR, 
                    justify=tk.CENTER, font=FONT, width=4, height=2
                )
                cell_label.grid()
                row.append(cell_label)
            self.cells.append(row)
        
        self.window.bind("<Key>", self.handle_keypress)

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2

    def compress(self):
        new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            pos = 0
            for j in range(GRID_SIZE):
                if self.grid[i][j] != 0:
                    new_grid[i][pos] = self.grid[i][j]
                    pos += 1
        self.grid = new_grid

    def merge(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE - 1):
                if self.grid[i][j] == self.grid[i][j + 1] and self.grid[i][j] != 0:
                    self.grid[i][j] *= 2
                    self.grid[i][j + 1] = 0

    def reverse(self):
        for i in range(GRID_SIZE):
            self.grid[i].reverse()

    def transpose(self):
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_left(self):
        self.compress()
        self.merge()
        self.compress()

    def move_right(self):
        self.reverse()
        self.move_left()
        self.reverse()

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def handle_keypress(self, event):
        if not self.game_over:
            key = event.keysym
            if key in ("Up", "Down", "Left", "Right"):
                old_grid = [row[:] for row in self.grid]
                if key == "Up":
                    self.move_up()
                elif key == "Down":
                    self.move_down()
                elif key == "Left":
                    self.move_left()
                elif key == "Right":
                    self.move_right()
                
                if self.grid != old_grid:
                    self.add_random_tile()
                    self.update_ui()
                    if self.is_game_over():
                        self.game_over = True
                        self.show_game_over()

    def update_ui(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.grid[i][j]
                if value == 0:
                    self.cells[i][j].config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    self.cells[i][j].config(
                        text=str(value),
                        bg=CELL_COLORS.get(value, "#3c3a32"),
                        fg=TEXT_COLORS.get(value, "#f9f6f2")
                    )
        self.window.update_idletasks()

    def is_game_over(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    return False
                if i < GRID_SIZE - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j < GRID_SIZE - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True

    def show_game_over(self):
        game_over_label = tk.Label(
            self.frame, text="Game Over!", font=FONT, fg="red", bg=BACKGROUND_COLOR
        )
        game_over_label.grid(row=2, column=0, columnspan=4)
        restart_button = tk.Button(
            self.window, text="Restart", font=FONT, command=self.restart_game
        )
        restart_button.pack(pady=10)

    def restart_game(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.game_over = False
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def start(self):
        self.window.mainloop()

# Start the game
if __name__ == "__main__":
    game = Game2048()
    game.start()
