gate1 = False    
gate2 = False
gate3 = False

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
        
print("Done")
