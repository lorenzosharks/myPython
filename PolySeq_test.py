import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image, ImageTk

import numpy as np

np.set_printoptions(precision = 2, suppress = True)

gate1 = False    
gate2 = False
gate3 = False

#------------------------------------------------------------------------

terms = 0


def ctol():
    # Get the text from the input box (entry widget)
    input_text = pdegree_entry.get()
    input_text2 = nseen_entry.get()
    input_text3 = nsums_entry.get()
    
    pdegree_entry.destroy()
    nseen_entry.destroy()
    nsums_entry.destroy()

    # Create a new label with the text from the entry
    pde1 = ttk.Label(mainframe, text=input_text).grid(column=2, row=1, sticky=W)
    
    pde2 = ttk.Label(mainframe, text=input_text2).grid(column=2, row=2, sticky=W)
    
    pde3 = ttk.Label(mainframe, text=input_text3).grid(column=2, row=3, sticky=W)

def create(*args):
    skibidi.destroy()
    try:        
        root.unbind("<Return>")
        # Create a list to store IntVars for each entry box
        global entry_vars
        entry_vars = []
        value = int(pdegree.get())
        
        images = []

        # This will store references to images to prevent garbage collection

        def render_latex_to_image(latex_code):
            # Create a figure with transparent background
            fig = Figure(figsize=(2, 1), facecolor='none', edgecolor='none')
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
            ax.axis('off')  # Turn off the axis
            
            # Use tight_layout to minimize whitespace
            fig.tight_layout(pad=0)

            # Create a canvas and draw the figure on it
            canvas = FigureCanvas(fig)
            canvas.draw()
            
            # Save to a buffer
            buf = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8)
            width, height = canvas.get_width_height()
            
            img = buf.reshape(height, width, 4)  # Image is in RGBA format
            img = Image.fromarray(img, 'RGBA')  # Create an RGBA image
            
            return img
        
        def display_latex(index):
            latex_code = f"a_{{{index}}}"  # Your LaTeX code here
            img = render_latex_to_image(latex_code)
            img = img.resize((100, 50), Image.LANCZOS)  # Resize to desired dimensions
            img_tk = ImageTk.PhotoImage(img)
            images.append(img_tk)  # Keep a reference to prevent garbage collection
            return img_tk
        
        eye=0
        
        for i in range(value):  
            img_tk = display_latex(i)  # Get the resized image for the label
            
            # Create a label with the LaTeX image
            label = ttk.Label(mainframe, image=img_tk)
            label.grid(column=1, row=i + 4, sticky=E)
            
            # Create a new IntVar for each entry box
            entry_var = IntVar()
            entry_vars.append(entry_var)  # Add to the list
            
            # Create an entry box next to the label
            entry = ttk.Entry(mainframe, width=7, textvariable=entry_var)
            entry.grid(column=2, row=i + 4, sticky=(tk.W, tk.E))
            
            eye = eye+1
        
        calculation = ttk.Button(mainframe, text="Confirm", command=polynomial_creation)
        calculation.grid(column=3, row=eye+4, sticky=W)

    except ValueError:
        pass
def two():
    ctol()
    create()
    
def polynomial_creation():
    print_entry_vars()
    polynomial()
    
    
def print_entry_vars():
    global list
    list = [entry_var.get() for entry_var in entry_vars]
    
def polynomial():
        # This will store references to images to prevent garbage collection
        images = []
        value = int(pdegree.get())
        label = []
        images1 = []

        def render_latex_to_image(latex_code):
            # Create a figure with transparent background
            fig = Figure(figsize=(2, 1), facecolor='none', edgecolor='none')
            ax = fig.add_subplot(111)
            ax.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
            ax.axis('off')  # Turn off the axis
             
            # Use tight_layout to minimize whitespace
            fig.tight_layout(pad=0)

            # Create a canvas and draw the figure on it
            canvas = FigureCanvas(fig)
            canvas.draw()
            
            # Save to a buffer
            buf = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8)
            width, height = canvas.get_width_height()
            
            img = buf.reshape(height, width, 4)  # Image is in RGBA format
            img = Image.fromarray(img, 'RGBA')  # Create an RGBA image
            
            return img
            
        def display_latex2(index):
            latex_code = f"x^{{{index}}}"  # Your LaTeX code here
            img = render_latex_to_image(latex_code)
            img = img.resize((100, 50), Image.LANCZOS)  # Resize to desired dimensions
            img_tk = ImageTk.PhotoImage(img)
            images1.append(img_tk)  # Keep a reference to prevent garbage collection
            return img_tk
        
        
        a = value + 4
        
        for i in range(value):  

            # Create an label behind the label
            entry_label = ttk.Label(mainframe, text=f"{list[i]}")
            entry_label.grid(column=i, row=a+1, sticky=(tk.W, tk.E))
            
            img_tk = display_latex2(i)  # Get the resized image for the label
            
            # Create a label with the LaTeX image
            label = ttk.Label(mainframe, image=img_tk)
            label.grid(column=i+1, row=a+1, sticky=(W, E))
            
        
        description = ttk.Label(mainframe, text = "This sequence is defined by y =").grid(column=1, row=a, sticky=(W, E))
#------------------------------------------------------------------------

root = Tk()
root.title("Polynomial Sequence")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#------------------------------------------------------------------------

pdegree = IntVar()
pdegree_entry = ttk.Entry(mainframe, width=7, textvariable=pdegree)
pdegree_entry.grid(column=2, row=1, sticky=(W, E))

nseen = IntVar()
nseen_entry = ttk.Entry(mainframe, width=7, textvariable=nseen)
nseen_entry.grid(column=2, row=2, sticky=(W, E))

nsums = IntVar()
nsums_entry = ttk.Entry(mainframe, width=7, textvariable=nsums)
nsums_entry.grid(column=2, row=3, sticky=(W, E))

#------------------------------------------------------------------------

ttk.Label(mainframe, text="Highest Polynomial Degree").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Terms seen").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Number terms added").grid(column=1, row=3, sticky=W)

#------------------------------------------------------------------------

skibidi = ttk.Button(mainframe, text="Confirm", command= two)
skibidi.grid(column=3, row=3, sticky=W)

#------------------------------------------------------------------------

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", two)

root.mainloop()

"""
while gate1 == False:
    try:
        try:
            poly_degree = abs(int(input("What is the degree of the polynomial: ")))
            gate1 = True
        except ValueError as ve:
            print("Enter a whole number.")
    except ValueError as ve:
        print("Enter a whole number.")
    
while gate2 == False:
    try:
        try:
            num_terms = abs(int(input("How many terms do you want to see: ")))
            gate2 = True
        except ValueError as ve:
            print("Enter a whole number.")
    except ValueError as ve:
        print("Enter a whole number.")
       
while gate3 == False: 
    try:
        try:
            sum_terms = abs(int(input("How many terms are added in the sum: ")))
            gate3 = True
        except ValueError as ve:
            print("Enter a whole number.")
    except ValueError as ve:
        print("Enter a whole number.")
    
#------------------------------------------------------------------------

i=0
pd_list = []

proceed2 = False

while i <= poly_degree:
    while proceed2 == False:
        try:
            term = float(input(f"a_{i}: "))
            try:
                proceed2 = True
            except ValueError as ve:
                print("Enter a number.")
        except ValueError as ve:
            print("Enter a number.")
    
    if proceed2 == True:
        pd_list.append(term)
        i = i+1
        proceed2 = False

pd_list = np.array(pd_list)

#------------------------------------------------------------------------

degree = 0

number_sum = []

final_sum = []

iterations = 0

if sum_terms > num_terms:
    a = sum_terms
elif sum_terms <= num_terms:
    a = num_terms

while iterations < a:

    while degree <= poly_degree:
        number_sum.append(pd_list[degree]*((iterations+1)**degree))
        degree = degree+1

    degree = 0

    final_sum.append(np.sum(number_sum))
    number_sum = []
    iterations = iterations+1

final_sum = np.array(final_sum)

#------------------------------------------------------------------------

#Note: NOT stands for number of terms

def linear_sum(NOT):
    top = 1+NOT
    
    l_sum = (top/2)*NOT

    return l_sum

def quadratic_sum(NOT):
    top = (NOT)*(NOT+1)*(2*NOT+1)

    q_sum = top/6

    return q_sum

def cubic_sum(NOT):
    top = ((NOT**2)+NOT)**2

    c_sum = top/4

    return c_sum

#------------------------------------------------------------------------

if poly_degree == 0:

    series_sum = num_terms*final_sum[0]

elif poly_degree == 1:
    
    series_sum = linear_sum(num_terms)

elif poly_degree == 2:

    term1 = pd_list[0] * num_terms
    term2 = pd_list[1] * linear_sum(num_terms)
    term3 = pd_list[2] * quadratic_sum(num_terms)

    series_sum = term1+term2+term3

elif poly_degree == 3:

    term1 = pd_list[0] * num_terms
    term2 = pd_list[1] * linear_sum(num_terms)
    term3 = pd_list[2] * quadratic_sum(num_terms)
    term4 = pd_list[3] * cubic_sum(num_terms)

    series_sum = term1+term2+term3+term4

#------------------------------------------------------------------------

i = 0

sign = ""

print("This sequence is defined by y =", end="")

while i <= poly_degree:

    if i == 0 and pd_list[0] >= 0:
        sign = ""
    elif pd_list[i] < 0:
        sign = "-"
    else:
        sign = "+"

    print(f" {sign} {abs(pd_list[i])}x^{i}", end="")
    i = i+1

print()

#------------------------------------------------------------------------

if num_terms <= 1:
    grammar = "term"
else:
    grammar = "terms"


print(f"The first {num_terms} {grammar} are: ")


print(np.round(final_sum, 2))


avalible_summations = [0, 1, 2, 3]


if poly_degree in avalible_summations:
    print(f"The sum of the first {sum_terms} terms is {np.round(series_sum, 2)}.")
else:
    print(f"The sum formulas for {poly_degree} degrees is not implemented yet.")
"""
