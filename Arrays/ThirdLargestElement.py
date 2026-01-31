#Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.
def find_third_largest(arr):
    if len(arr) < 3:
        return -1
    first = second = third = float('-inf')
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num
    return third if third != float('-inf') else -1
n = int(input("Enter the number of elements in the array: "))
arr = []
for _ in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
third_largest = find_third_largest(arr)
if third_largest != -1: 
    print("The third largest element is:", third_largest)
else:
    print("The third largest element is not found")