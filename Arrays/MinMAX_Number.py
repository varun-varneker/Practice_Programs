#Given an array arr[]. Your task is to find the minimum and maximum elements in the array.
def find_min_max(arr):
    if not arr:
        return None, None
    min_element = arr[0]
    max_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num
    return min_element, max_element
n = int(input("Enter the number of elements in the array: "))
arr = []
for _ in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
min_element, max_element = find_min_max(arr)
print("Minimum element:", min_element)
print("Maximum element:", max_element)