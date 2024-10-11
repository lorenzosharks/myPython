# Karson xu, Honors Precalculus, 10/10/2024

# Assignment 1 Polynomial Sequences

# The program prompts the user to enter the coefficients of the explicit formula
# of a polynomial sequence , the number of terms they want to see, and 
# the number of terms they want to sum. It then prints out 
# the equation, the terms they requested, and if possible,
# the sum that they requested.



import numpy as np

gate1 = False
gate2 = False
gate3 = False

while gate1 == False and gate2 == False and gate3 == False:
    try:
        poly_degree = abs(int(input("What is the degree of the polynomial: ")))
        try:

            gate1 = True
            
            try:
                num_terms = abs(int(input("How many terms do you want to see: ")))
                try:

                    gate2 = True

                    try:
                        sum_terms = abs(int(input("How many terms are added in the sum: ")))
                        try:
                            
                            gate3 = True
                        
                        except ValueError as ve:
                            print("Enter a whole number.")
                    except ValueError as ve:
                        print("Enter a whole number.")
                
                except ValueError as ve:
                    print("Enter a whole number.")
            except ValueError as ve:
                print("Enter a whole number.")
        
        except ValueError as ve:
            print("Enter a whole number.")
    except ValueError as ve:
        print("Enter a whole number.")


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
