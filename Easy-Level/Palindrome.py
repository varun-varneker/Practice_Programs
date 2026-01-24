#You are given an integer n. Your task is to determine whether it is a palindrome.
def is_palindrome(n):
    n = n.lower()
    original_n = str(n)
    reversed_n = original_n[::-1]
    return original_n == reversed_n
n = input("Enter a word: ")
if is_palindrome(n):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")   
