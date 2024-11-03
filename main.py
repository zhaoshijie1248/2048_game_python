import game_functions as gf

def main():
    grid = gf.initialize_grid()
    while True:
        gf.print_grid(grid)
        
        if gf.is_game_won(grid):
            print("Congratulations! You've won the game!")
            break
        if not gf.is_move_possible(grid):
            print("Game Over! No more moves possible.")
            break
        
        move = input("Enter move (w/a/s/d): ").strip().lower()
        
        if move == 'w':
            new_grid = gf.move_up(grid)
        elif move == 's':
            new_grid = gf.move_down(grid)
        elif move == 'a':
            new_grid = gf.move_left(grid)
        elif move == 'd':
            new_grid = gf.move_right(grid)
        else:
            print("Invalid input! Please use 'w', 'a', 's', or 'd' to move.")
            continue
        
        if new_grid != grid:
            grid = new_grid
            gf.add_random_tile(grid)
        else:
            print("Move not possible. Try a different direction.")
            
if __name__ == "__main__":
    main()
