# """Karson Xu, Honors Precalculus, 1/27/2024"""
# """Honors Precalculus: Programming Assignment 2"""
# """This program takes in the coefficients of a polynomial sequence and the degree of the polynomial. It then prints a string representation of the function and its derivative as well as plot both of the functions on a graph. """

#Importing functions
import numpy as np
import matplotlib.pyplot as plt

#Formatting the final answer
np.set_printoptions(precision = 2, suppress = True)

# #Functions
def getCoeffs(order):
    """
    summary: coefficients of the polynomial
    parameters: none
    return: return array of coeffecients
    """
    
    flag = False

    while flag == False:
        try:
            poly_degree = int(input(f"What is the highest degree of the {order} polynomial: "))
            try:
                flag = True
            except ValueError as ve:
                print("Enter a number.")
        except ValueError as ve:
            print("Enter a number.")
    
    
    coeff_array = []
    i=poly_degree
    proceed2 = False

    
    while i != -1:
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
            i = i-1 
            proceed2 = False
            
    coeff_array = list(reversed(coeff_array))
            
    return np.array(coeff_array)

def polyToStr(coeff_array):

    """
    summary:creates a string representation of a polynomial equation.
    parameters: polynomial coefficient array
    return: returns the string representation of the polynomial equation
    """

    sign = ""
    
    poly_degree = len(coeff_array) - 1
    
    i = poly_degree
    
    polyStr = ""
    
    while i != -1:
        
        if i == poly_degree and coeff_array[poly_degree] >= 0:
            sign = ""
        elif coeff_array[i] < 0:
            sign = "-"
        else:
            sign = "+"
    
        polyStr += f"{sign} {abs(coeff_array[i])}x^{i}" if i == 0 and coeff_array[0] > 0 else f" {sign} {abs(coeff_array[i])}x^{i}"

        i = i-1
    
    return polyStr

# #--------------------------------------------------------------------------------------------------------#
# #--------------------------------------------------------------------------------------------------------#

# #Main program

#Prompting for coefficients of both polynomials
coeff_arr1 = getCoeffs("first")
        
coeff_arr2 = getCoeffs("second")


#Calculating for the coefficients of the product
pre_sum_array = np.outer(coeff_arr1, coeff_arr2)

psa = pre_sum_array

diagonals = [np.flipud(psa).diagonal(offset=i).tolist() for i in range(-psa.shape[0] + 1, psa.shape[1])]

sums = [sum(diagonal) for diagonal in diagonals]


#Print statements
print("This is the product of the two polynomials: ")
print(polyToStr(sums))