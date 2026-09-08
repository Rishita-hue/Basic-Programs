# Program to calculate the BMI of the body
Weight=int(input("Enter the weight of the body in kg:"))
Height=float(input("Enter the height of the body in m:"))
BMI=Weight/Height**2
print("The BMI of the person is",round(BMI,2))