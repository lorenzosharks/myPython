"""Karson Xu, Honors Precalculus, 1/27/2024"""
"""Honors Precalculus: Programming Assignment 2"""
"""This program takes in the coefficients of a polynomial sequence and the degree of the polynomial. It then prints a string representation of the function and its derivative as well as plot both of the functions on a graph. """

#Importing functions
import numpy as np
import matplotlib.pyplot as plt

#Formatting the final answer
np.set_printoptions(precision = 2, suppress = True)

#Functions
def getCoeffs():
    """
    summary: coefficients of the polynomial
    parameters: none
    return: return array of coeffecients
    """
    
    flag = False

    while flag == False:
        try:
            poly_degree = float(input(f"What is the highest degree of the polynomial: "))
            try:
                flag = True
            except ValueError as ve:
                print("Enter a number.")
        except ValueError as ve:
            print("Enter a number.")
    
    coeff_array = []
    i=0
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
            coeff_array.append(term)
            i = i+1 
            proceed2 = False
            
    coeff_array = np.array(coeff_array)
            
    return np.array(coeff_array)

def polyToStr(coeff_array):

    """
    summary:creates a string representation of a polynomial equation.
    parameters: polynomial coefficient array
    return: returns the string representation of the polynomial equation
    """
    i = 0

    sign = ""
    
    poly_degree = len(coeff_array) - 1
    
    polyStr = ""
    
    while i <= poly_degree:
    
        if i == 0 and coeff_array[0] >= 0:
            sign = ""
        elif coeff_array[i] < 0:
            sign = "-"
        else:
            sign = "+"
    
        polyStr += f"{sign} {abs(coeff_array[i])}x^{i}" if i == 0 and coeff_array[0] > 0 else f" {sign} {abs(coeff_array[i])}x^{i}"

        i = i+1
    
    return polyStr

def polyEval(coeff_array, x_array):

    """
    summary: Calculates the outputs of the polynomial
    parameters: coefficient array and array with the inputs of the equation
    return: array with outputs
    """
    polyDegree = len(coeff_array)
    
    # exponent = 0
    
    exponents =  np.arange(polyDegree)    
    
    pre_terms = np.power(x_array[:, np.newaxis], exponents)
    pre_terms = np.array(pre_terms)

    terms = pre_terms * coeff_array
        
    output = np.sum(terms, axis = 1)
    
    return np.array(output) # np.array(output)

def polyDiff(coeff_array):

    """
    summary: Calculates the derivative of the polynomial
    parameters: coefficient array of original function 
    return: the coefficient array of the derivative
    """
    
    exponents = np.arange(len(coeff_array))

    diff_coeff = np.array(coeff_array) * np.array(exponents)
    
    diff_coeff = np.delete(diff_coeff, 0)
    
    return np.array(diff_coeff)

#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

#Main program


#Asking the user for the degree of the polynomial (Includes user proofing)
             
coeff_array = getCoeffs()

#The math part
diff_array = polyDiff(coeff_array)

#--------------------------------------------------------------------------------------------------------#

#Display part

#plot formatting
plt.figure(figsize=(6, 6)) #Limit the size of the graph

plt.axhline(0, color = "black", lw = 1) # x-axis
plt.axvline(0, color = "black", lw = 1) # y-axis

plt.grid(True) #Adds a grid so theres a reference

plt.axis('scaled') #Making the grid look nice

plt.xlim(-10, 10) # Set the limits of the x-axis
plt.ylim(-10, 10) # Set the limits of the y-axis


#Lables
plt.xlabel("x axis") 
plt.ylabel("y axis")
plt.title("f(x) and its derivative")


#Actual plotting
x = np.linspace(-100, 100, 2000000) # Creating an array of the x coordinates

y = polyEval(coeff_array, x) # f(x)
diffy = polyEval(diff_array, x) # f'(x)

plt.plot(x, y, label = "f(x)", color = "red") # plotting f(x)
plt.plot(x, diffy, label = "f'(x)", color = "blue") # plotting f'(x)




#Print statements
print("This is the function:")
print(f"f(x) ={polyToStr(coeff_array)}")

print("")

print("This is the derivative function:")
print(f"f'(x) ={polyToStr(diff_array)}")

plt.legend()
plt.show()