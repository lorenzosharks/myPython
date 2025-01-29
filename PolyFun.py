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
    
    poly_degree = len(coeff_array) - 1
    
    polyStr = "f(x) ="
    
    while i <= poly_degree:
    
        if i == 0 and coeff_array[0] >= 0:
            sign = ""
        elif coeff_array[i] < 0:
            sign = "-"
        else:
            sign = "+"
    
        polyStr += f"{sign} {abs(coeff_array[i])}n^{i}" if i == 0 and coeff_array[0] > 0 else f" {sign} {abs(coeff_array[i])}n^{i}"

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
    i=0
    input = 0
    terms = []
    output = []
    
    for input in range(len(x_array)):    
        
        for i in range(polyDegree):
            value = x_array[input]**i * coeff_array[i]
            terms.append(value)
            i = i + 1
        
        output.append(np.sum(terms))
        
        i=0
        terms = []
        input = input+1   
    
    return np.array(output)

def polyDiff(coeff_array):

    """
    summary: Calculates the derivative of the polynomial
    parameters: coefficient array of original function 
    return: the coefficient array of the derivative
    """
    position = 0
    diff_coeff = []
    
    for position in range(len(coeff_array)):
        diff_term = coeff_array[position] - 1
        
        diff_coeff.append(diff_term)
        
        position = position + 1
    
    return np.array(diff_coeff)

#Main program

#Asking the user for the degree of the polynomial

coeff_array = [1,2,3,4]
x_array = [0, 1, 2, 3]

print(polyToStr(coeff_array))

