#You are given a 3-digit number n, Find whether it is an Armstrong number or not.
def is_armstrong(n):
    original_n = n
    sum_of_cubes = 0

    while n > 0:
        digit = n % 10
        sum_of_cubes += digit ** 3
        n //= 10

    return sum_of_cubes == original_n
n = int(input("Enter a 3-digit number: "))
if 100 <= n <= 999:
    if is_armstrong(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")