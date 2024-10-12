# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)


# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk

# Sample data
sample_list = ["A", "B", "C", "D"]  # Ensure this has enough elements

# Create the main application window
root = tk.Tk()
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

def display_latex2(index):
    # This function should create and return the image for LaTeX
    latex_code = f"a_{{{index + 1}}}"  # Example LaTeX code
    fig = Figure(figsize=(2, 1), facecolor='none', edgecolor='none')
    ax = fig.add_subplot(111)
    ax.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
    ax.axis('off')  # Turn off the axis
    fig.tight_layout(pad=0)

    canvas = FigureCanvas(fig)
    canvas.draw()
    
    buf = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8)
    width, height = canvas.get_width_height()
    img = buf.reshape(height, width, 4)  # Image is in RGBA format
    img = Image.fromarray(img, 'RGBA')
    img_tk = ImageTk.PhotoImage(img)  # Convert to PhotoImage
    return img_tk

def create(value):
    for i in range(value):
        img_tk = display_latex2(i)  # Get the resized image for the label
        
        # Create a label with the LaTeX image
        label = ttk.Label(mainframe, image=img_tk)
        label.image = img_tk  # Keep a reference to avoid garbage collection
        label.grid(column=i + 1, row=1, sticky=(tk.W, tk.E))  # Adjust row as needed
        
        # Create a label behind the label with corresponding text
        entry_label = ttk.Label(mainframe, text=f"{sample_list[i]}")
        entry_label.grid(column=i, row=1, sticky=(tk.W, tk.E))  # Adjust row as needed

# Start creating widgets
create(len(sample_list))

# Run the application
root.mainloop()
