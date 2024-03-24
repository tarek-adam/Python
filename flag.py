import tkinter as tk
import random

# Define the Cell class
class Cell:
    # Constructor method (__init__)
    def __init__(self, master, row, col, button, count):
        # Initialize instance attributes
        self.master = master  # Parent widget (e.g., root window)
        self.row = row        # Row position of the cell in the grid
        self.col = col        # Column position of the cell in the grid
        self.button = button  # Button widget associated with the cell
        self.count = count    # Number of mines adjacent to the cell
        self.pressed = False  # Flag to track if the cell has been pressed
        self.flagged = False  # Flag to track if the cell is flagged
        self.button.bind("<Button -3>", self.flag)  # Bind right-click event to flag method
        # Configure the button and place it in the grid
        self.configure_button()
        self.place_button()

    # Method to configure the button's command
    def configure_button(self):
        # Set the button's command to call the button_click method of this Cell instance
        self.button.config(command=self.button_click)

    # Method to place the button in the Tkinter grid
    def place_button(self):
        # Place the button in the grid at the specified row and column
        self.button.grid(row=self.row, column=self.col, padx=1, pady=1)

    # Method to handle button clicks
    def button_click(self):
        # Print the row and column of the clicked cell
        print(f"Button clicked at row {self.row}, column {self.col}")
        # Check if the cell has already been pressed
    def press(self):
        """Button pressed.  Show bomb info"""
        if not self.pressed:
            self.configure(relief=tk.SUNKEN)
            self.pressed = True
            self.button['text'] = 'X' if self.count < 0 else str(self.count)
    # Method to handle right-clicks (flag)
    def flag(self, event):
        """Right mouse button click pressed.   Toggle flag marker"""
        if not self.pressed:
            self.flagged = not self.flagged
            flag_icon = "🚩"
            self.button['text'] = flag_icon if self.flagged else ''
    

# Main function to create and run the Tkinter application
def main():
    # Create the Tkinter root window
    root = tk.Tk()
    # Create a 10x10 grid of cells
    for i in range(10):
        for j in range(10):
            # Create a button widget for each cell
            button = tk.Button(root, text="", width=1, height=1)
            # Assign a random count value for the current cell
            count = random.randint(0, 8)
            # Create a Cell instance for the current cell
            cell = Cell(root, i, j, button, count)
    # Start the Tkinter event loop
    root.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the application
    main()