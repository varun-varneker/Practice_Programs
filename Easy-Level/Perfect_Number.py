#Given a number n, check if the number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.
def is_perfect_number(n):
    if n < 1:
        return False
    sum_of_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_factors += i
    return sum_of_factors == n
n = int(input("Enter a positive integer: "))
if is_perfect_number(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")