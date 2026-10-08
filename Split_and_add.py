# Program to split and add the splited parts of the  array 
def split_and_add(arr,d):
    l = len(arr)
    if d == 0:
        return 'Enter a non-zero number'
    if d >l:
        return 'Enter the number less than',l

    first_part = arr[:d]
    second_part = arr[d:]

    result = second_part+first_part

    return result


arr = list(map(int,input("Enter the elements of an array").split()))

d = int(input("Enter the number on what difference you want to split the array"))
result = split_and_add(arr,d)
print(result)

