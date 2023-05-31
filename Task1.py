"""Task 1: Recursion with no return (no unwinding)
Create a recursive function named countdown with a single integer input argument that prints a countdown starting from the given number.

Then, use the following test case:

countdown(5)
Your result should look like this:
5
4
3
2
1
0"""

# Solution
def countdown(n):
    if n >= 0:
        print(n)
        countdown(n - 1)

countdown(55)
