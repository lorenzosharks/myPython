scores = [4.0, 3.5, 3.2, 4.2, 4.0, 4.3, 2.5]

ii = 0
while ii < len(scores):
    print(f"Problem {int(ii)+1}: {str(scores[ii])}")
    ii = ii + 1

i=1
a = scores[0]

while i < len(scores):
    a = a+scores[i]
    i=i+1

print(f"Average: {round((a/(len(scores))), 2)}")