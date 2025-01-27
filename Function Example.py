### Intro stuff (name, date, program name)

### Import modules/libraries

### Functions (these live here, defined BEFORE - not in - the main program)

def numQuadZeros(a,b,c):
    """
    summary: this function determines the number of zeros for a quadratic, ax^2+bx+c 
    parameter(s): coefficients to the quadratic (type: floats)
    return: a message with number of zeros (type: str)
    """
    disc = b*b - 4*a*c
    if disc > 0:
        message = "two real zeros"
    elif disc == 0:
        message = "one real zero"
    else:
        message = "no real zeros"
        
    return message
       
def vertex(a, b, c):
    """
    summary: this function determines the vertex of a parabola, ax^2+bx+c
    parameter: coefficients of the quadratic (not including the constant)
    return: x and y coordinates of the vertex
    """
    
    x = -b/(2*a)
    
    y = a*(x**2) + b*x + c
    
    return x, y


######## MAIN PROGRAM ########

### INPUTS ###

# get coefficients for quadratic from the user
c2 = float(input("Enter the coeffient for the quadratic term in a quadratic equation: "))
c1 = float(input("Enter the coeffient for the linear term in a quadratic equation: "))
c0 = float(input("Enter the coeffient for the constant term in a quadratic equation: "))


### CALCULATIONS ###

# call the numQuadZeros function and save the "return" as a variable
dispNumZeros = numQuadZeros(c2,c1,c0)
vertexX, vertexY = vertex(c2,c1,c0)

### OUTPUTS ###
  
# display message re: number of zeros for their quadratic
print(f"For your quadratic function, there is/are {dispNumZeros} and the vertex is at ({vertexX}, {vertexY}).")

