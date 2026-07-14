n = int(input("Enter any number:"))
factorial = 1
if n < 0:
  print("Factorial does not exist for a negative number")
elif n == 0:
  print("Factorial of 0 is 1")
else:
  for i in range(1,n+1):
    factorial = factorial*i
  print("The factorial of",n,"is",factorial)