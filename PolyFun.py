"""Karson Xu, Honors Precalculus, 1/27/2024"""
"""Honors Precalculus: Programming Assignment 2"""
"""This program takes in the coefficients of a polynomial sequence and the degree of the polynomial. It then prints a string representation of the function and its derivative as well as plot both of the functions on a graph. """


#Importing functions
import numpy as np
import matplotlib.pyplot as plt


#Functions

def getCoeffs(poly_degree):
    """
summary: coefficients of the polynomial
parameters: none
return: return array of coeffecients
"""
    
    pd_list = []
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
            pd_list.append(term)
            i = i+1 
            proceed2 = False
            
    pd_list = np.array(pd_list)
            
    return pd_list


def polyToStr(coeff_array):

    """
    summary:creates a string representation of a polynomial equation.
    parameters: polynomial coefficient array
    return: returns the string representation of the polynomial equation
    """
    i = 0

    sign = ""
    
    print("This sequence is defined by f(x) =", end="")
    
    while i <= poly_degree:
    
        if i == 0 and coeff_array[0] >= 0:
            sign = ""
        elif coeff_array[i] < 0:
            sign = "-"
        else:
            sign = "+"
    
        polyStr= print(f"{sign} {abs(coeff_array[i])}n^{i}", end="")

        i = i+1
    
    return polyStr





def polyEval():

    """
    summary: Calculates the outputs of the polynomial
    parameters: coefficient array and array with the inputs of the equation
    return: array with outputs
    """

    return None






def polyDiff():

    """
    summary: Calculates the derivative of the polynomial
    parameters: coefficient array of original function 
    return: the coefficient array of the derivative
    """

    return None

#Main program

#Asking the user for the degree of the polynomial

poly_degree = int(input("Enter the degree of the polynomial: "))

a = getCoeffs(poly_degree)

print(polyToStr(a))

print(a)


