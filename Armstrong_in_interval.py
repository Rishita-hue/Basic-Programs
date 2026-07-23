a = int(input("Enter upper limit:"))
b = int(input("Enter lower limit:"))
total = 0
for i in range (a,b+1):
    order = len(str(i))
    c = int(i)**order
    total += c
if total == int(i):
    print(i)