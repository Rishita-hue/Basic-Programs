#Program to calculate the cube sum of n natural numbers
def cube_sum(n):
    if n<=0:
        print("Enter a positive number")
        
    else:
        result=sum([i**3 for i in range(1,n+1)])
        return result

print(cube_sum(5))

