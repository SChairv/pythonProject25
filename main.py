#Easy: Create a function that takes an integer
#and returns the factorial of that integer.

def factorial(n):
    factorial = 1
    b = n
    while b > 0:
        factorial = factorial * b
        b = b - 1

    return factorial


n = int(input("Please enter a number to find a factorial for "))

print("The factorial of ", n, "is ", factorial(n), ".")
