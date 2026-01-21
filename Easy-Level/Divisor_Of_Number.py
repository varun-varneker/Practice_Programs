#Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.

n = int(input("Enter a number: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print("The divisors of the given number are:", divisors)