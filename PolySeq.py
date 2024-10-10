"This program solves for the first n terms given the equation and also solves for the sum of the first n terms if applicable"

import numpy as np

proceed = False

while proceed == False:
    try:
        poly_degree = 2 ## abs(int(input("What is the degree of the polynomial: ")))
        num_terms = 2 ## abs(int(input("How many terms do you want to see: ")))
        sum_terms = 2 ## abs(int(input("How many terms are added in the sum: ")))
        try:
            proceed = True
        except ValueError as ve:
            print("Enter a whole number.")
    except ValueError as ve:
        print("Enter a whole number.")

i=0
pd_list = []

while i <= poly_degree:
    pd_list.append(float(input(f"a_{i}: ")))
    i = i+1

pd_list = np.array(pd_list)

i = 0

print(pd_list)

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


