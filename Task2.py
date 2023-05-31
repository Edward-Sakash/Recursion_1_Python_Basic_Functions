"""Task 2: Recursion with return and instructions after return (non tail-recursive)
Create a recursive function named factorial that returns the factorial of a number (the number multiplied by every integer lower than the number and greater than 0).

Then, use the following test cases:

print(factorial(0))
print(factorial(1))
print(factorial(10))
Your result should look like this:
1
1
3628800"""

# Solution 
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: multiply n by factorial of (n-1)
        return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(10))
print(factorial(20))
