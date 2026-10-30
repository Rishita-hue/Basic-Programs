# Program to sort words or a list alphabatically
result = []
String = input("Enter a string:").split()
new_string = sorted(String)
for i in new_string:
    a = i.capitalize()
    result.append(a)
b = " ".join(result)
print("The sorted words are:",b)
