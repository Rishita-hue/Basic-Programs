#Program to calculate the sum of array
my_list=list(input("Enter the elements of list:").split())
total=0
for i in my_list:
    total+= int(i)
print("The sum of array is",total)


#Program to calculate the sum of array using function
def sum_of_array(arr):
    total=0
    for i in arr:
        total+=i
    return total

arr=[1,2,3]
result=sum_of_array(arr)
print("The sum of array is",result)

#Program to calculate the sum of array using sum()
arr=[1,2,3]
result=sum(arr)
print("The sum of array is :",result)


