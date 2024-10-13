import tkinter as tk
from tkinter import Canvas

def resize_canvas(event):
    # Get the new width of the canvas when resized
    new_width = event.width
    # Clear any existing lines on the canvas
    separator_canvas.delete("all")
    # Redraw the line with the updated width
    separator_canvas.create_line(0, 2, new_width, 2, fill="black", width=3)

root = tk.Tk()

# Create the mainframe inside the root window
mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Create the canvas for the separator
separator_canvas = Canvas(mainframe, height=5, highlightthickness=0)
separator_canvas.grid(column=1, row=4, columnspan=10, sticky=(tk.W, tk.E))

# Bind the resize event of the canvas to dynamically redraw the line
separator_canvas.bind("<Configure>", resize_canvas)

# Ensure the column expands with the window
mainframe.grid_columnconfigure(1, weight=1)

# Ensure the window's grid expands
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)