# Fibonacci series
n = int(input("Enter the number till which you want the fibonacci series:"))
num1 = 0
num2 = 1
for i in range(n):
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result
    