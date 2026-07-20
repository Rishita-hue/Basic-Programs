# The program calculate weather the number is armstrong or not
n = input("Enter any number:")
total = 0
power = len(n)
for i in n:
    a = int(i)**power
    total += a
if total == int(n):
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")