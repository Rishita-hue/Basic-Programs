# The program perform arithmetic division of two numbers 
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
if n2 == 0:
    print("Enter a non-zero number for the second number.")
else:
    division = n1 /n2
print("The result of the division is:",division)