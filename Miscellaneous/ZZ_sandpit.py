import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Specific Position Window")

# Define the desired width, height, and coordinates
window_width = 400
window_height = 300
x_coordinate = 100  # X-coordinate from the left edge of the screen
y_coordinate = 500   # Y-coordinate from the top edge of the screen

# Set the window's geometry
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Start the Tkinter event loop
root.mainloop()