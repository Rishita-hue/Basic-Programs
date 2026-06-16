# Calculating the Quadratic equation
import math
a = float(input("Enter the cofficient of a:"))
b = float(input("Enter the cofficient of b:"))
c = float(input("Enter the cofficient of c:"))
 
# Calculate the discriminant of equation
D = b**2-4*a*c

# if D > 0 the equation will have two distinct roots
if D>0:
    root1 = (-b + math.sqrt(D))/(2*a)
    root2 = (-b - math.sqrt(D))/(2*a)
    print(f"root1: {root1}")
    print(f"root2:{root2}")
# if D = 0 the equation will have two equal roots
elif D == 0:
    root = -b/(2*a)
    print(f"root:{root}")
# if D < 0 the equation will have two complex roots
else:
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(D))/(2*a)
    print(f"root1:{real_part}+{imaginary_part}i")
    print(f"root2:{real_part}-{imaginary_part}i")



