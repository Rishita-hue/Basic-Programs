# Program to calculate if an array is monotonic or not
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i-1]:
            increasing = False

    return increasing or decreasing

arr = [1,2,2,3,4]

print("arr is monotonic:",is_monotonic(arr))