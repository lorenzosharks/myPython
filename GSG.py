import numpy as np

ratio = float(input("Ratio: "))
term1 = float(input("First term: "))
numTerms = int(input("# of terms: "))

indices = np.arange(1, numTerms + 1)
terms = term1 * ratio**(indices-1)

sequenceString = "{ "
ii = 0
while ii < numTerms:
    sequenceString = sequenceString + str(terms[ii]) + ","
    ii = ii + 1
sequenceString = sequenceString + "...}"

equationString = "g_k = " + str(term1) + "*" + str(ratio) + "^(k-1)"

print(f"The first {str(term1)} terms of {equationString} are: {sequenceString}")