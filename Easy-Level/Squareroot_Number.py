#Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.
def square_root(n):
    if n < 0:
        raise ValueError("Input must be a positive integer")
    return int(n**0.5)
n = int(input("Enter a positive integer: "))
result = square_root(n)
print("The square root (floor value) is:", result)