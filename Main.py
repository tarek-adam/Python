import tkinter as tk
import random


# Define the Cell class
class Cell:
    # Constructor method (__init__)
    def __init__(self, master, row, col, button, has_mine):
        # Initialize instance attributes
        self.master = master  # Parent widget (e.g., root window)
        self.row = row        # Row position of the cell in the grid
        self.col = col        # Column position of the cell in the grid
        self.button = button  # Button widget associated with the cell
        self.has_mine = has_mine  # Whether the cell has a mine
        self.neighbor_mines = 0  # Number of neighboring cells with mines
        self.flagged = False  # Whether the cell is flagged
        # Configure the button and place it in the grid
        self.configure_button()
        self.place_button()

    # Method to configure the button's command
    def configure_button(self):
        # Set the button's command to call the button_click method of this Cell instance
        self.button.bind("<Button-1>", self.button_left_click)
        self.button.bind("<Button-3>", self.button_right_click)

    # Method to place the button in the Tkinter grid
    def place_button(self):
        # Place the button in the grid at the specified row and column
        self.button.grid(row=self.row, column=self.col, padx=1, pady=1)

    # Method to handle left mouse clicks
    def button_left_click(self, event):
        # Check if the clicked cell has a mine
        if self.has_mine:
            print("Game Over! You clicked on a mine.")
            # Trigger game over actions (e.g., reveal all cells)
            self.master.reveal_all()
            # Optionally, you might want to end the game here
        else:
            # Print the row and column of the clicked cell
            print(f"Button clicked at row {self.row}, column {self.col}")
            # Show the number of neighboring mines if the cell is not empty
            if self.neighbor_mines > 0:
                self.button.config(text=str(self.neighbor_mines))
            else:
                # If the cell is empty, reveal its neighbors
                self.master.reveal_neighbors(self.row, self.col)

    # Method to handle right mouse clicks
    def button_right_click(self, event):
        # Toggle flag on the cell
        self.flagged = not self.flagged
        if self.flagged:
            self.button.config(text="🚩")  # Unicode flag emoji
        else:
            self.button.config(text="")  # Clear the text when removing the flag



# Define the Minesweeper class
class Minesweeper:
    # Constructor method (__init__)
    def __init__(self, root):
        self.root = root  # Root window
        self.cells = []   # List to store all cells

    # Method to create the game grid
    def create_grid(self):
        # Create a 10x10 grid of cells
        mine_positions = random.sample(range(100), 10)  # Get 10 unique random positions for mines
        for i in range(10):
            for j in range(10):
                # Create a button widget for each cell
                button = tk.Button(self.root, text="", width=1, height=1)
                # Check if the current position has a mine
                has_mine = (i * 10 + j) in mine_positions
                # Create a Cell instance for the current cell
                cell = Cell(self, i, j, button, has_mine)
                # Increment counters in surrounding cells if the current cell has a mine
                if has_mine:
                    self.increment_neighbor_counters(i, j)
                self.cells.append(cell)

    # Method to increment counters in surrounding cells
    def increment_neighbor_counters(self, row, col):
        for i in range(max(0, row - 1), min(row + 2, 10)):
            for j in range(max(0, col - 1), min(col + 2, 10)):
                if (i != row or j != col) and (i * 10 + j) < len(self.cells):
                    self.cells[i * 10 + j].neighbor_mines += 1

    # Method to reveal all cells
    def reveal_all(self):
        for cell in self.cells:
            if cell.has_mine:
                cell.button.config(text="MINE", state="disabled", fg="red", font=("Helvetica", 10, "bold"))
            elif cell.neighbor_mines > 0:
                cell.button.config(text=str(cell.neighbor_mines))
            else:
                cell.button.config(state="disabled")

    # Method to reveal neighboring cells recursively
    def reveal_neighbors(self, row, col):
        for i in range(max(0, row - 1), min(row + 2, 10)):
            for j in range(max(0, col - 1), min(col + 2, 10)):
                if (i != row or j != col) and (i * 10 + j) < len(self.cells):
                    cell = self.cells[i * 10 + j]
                    if cell.neighbor_mines > 0:
                        cell.button.config(text=str(cell.neighbor_mines))
                    else:
                        cell.button.config(state="disabled")
                        self.reveal_neighbors(i, j)



# Main function to create and run the Tkinter application
def main():
    # Create the Tkinter root window
    root = tk.Tk()
    # Create an instance of Minesweeper
    minesweeper = Minesweeper(root)
    # Create the game grid
    minesweeper.create_grid()
    # Start the Tkinter event loop
    root.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the application
    main()
