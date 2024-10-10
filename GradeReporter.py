grade = float(input("Grade: "))

if grade >= 93:
    print("A")
elif grade < 93 and grade >= 90:
    print("A-")
elif grade < 90 and grade >= 87:
    print("B+")
elif grade < 87 and grade >= 83:
    print("B")
elif grade < 83 and grade >= 80:
    print("B-")
elif grade < 80 and grade >= 77:
    print("C+")
elif grade < 77 and grade >= 73:
    print("C")
elif grade < 73 and grade >= 70:
    print("C-")
else:
    print("E")