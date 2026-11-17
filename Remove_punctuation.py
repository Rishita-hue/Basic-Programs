# Program to remove punctuation from the string
Punctuation = """!@#$%^&*()_-``~[]{};:""'<,>.?/ | + - """

my_string = input("Enter any string:")
result_string = ""
for i in my_string:
    if i in Punctuation:
        continue
    else:
        result_string +=i
print("The result_string is:",result_string)