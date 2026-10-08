#Program to calculate the largest element of an array 
arr=list(map(int,input("Enter the elements of an array:").split()))
big_no=arr[0]
for i in arr:
    if i > big_no:
        big_no=i

print("The largest element in array",big_no)