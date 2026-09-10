#Program to calculate the logrithm of any number
import math

num=float(input("Enter a number:"))

if num<=0:
    print("Please enter a positive number")
else:
    result=math.log(num)
    print("The natural logrithm of",num,"is",result)