"""Task 3: Recursion with return and instructions after return (non tail-recursive)
Create a function called harmonic_sum that requires an integer as an argument. The function will return the harmonic sum of the integer.

The harmonic sum is the sum of reciprocals of the positive integers. The harmonical sum of 2 is:

1/1 + 1/2 = 1.5

The harmonic sum of 4 is:

1/1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

Then, use the following test cases:

print(harmonic_sum(7))
print(harmonic_sum(4))
Your result should look like this:
2.5928571428571425
2.083333333333333"""

# Solution
def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)

print(harmonic_sum(7))
print(harmonic_sum(4))
