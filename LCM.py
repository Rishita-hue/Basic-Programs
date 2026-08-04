#Calculation of LCM of two numbers
a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))
maxnum = max(a,b)
while(True):
    if(maxnum%a==0 and maxnum%b==0):
        break
    maxnum = maxnum + 1

print(f"The LCM of {a} and {b} is {maxnum}")