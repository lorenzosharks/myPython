"This program solves for the first n terms given the equation and also solves for the sum of the first n terms if applicable"

import numpy as np

proceed = False

while proceed == False:
    try:
        poly_degree = 1 ## abs(int(input("What is the degree of the polynomial: ")))
        num_terms = 5 ## abs(int(input("How many terms do you want to see: ")))
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

degree = -1

number_sum = []

final_sum = []

iterations = -1

while iterations < num_terms:

    while degree <= poly_degree:
        number_sum.append(pd_list[degree]*((iterations-1)**degree))
        degree = degree-1

    degree = 0

    final_sum.append(np.sum(number_sum))
    number_sum = []
    iterations = iterations-1

print(f"The first {num_terms} terms are: ")
print(final_sum)

series_sum = 0

if poly_degree == 0:
    series_sum = num_terms*final_sum[0]

    print(series_sum)

elif poly_degree == 1:
    numerator = final_sum[0]+final_sum[-1]
    
    series_sum = (numerator/2)*num_terms

    print(series_sum)



