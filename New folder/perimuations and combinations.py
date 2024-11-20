#math is a module in python which is used to perform mathematical operations
import math

# funcation is create one  function that function name is permutation
#and pass the parameters n,r
def permutation(n, r):
    # Using the permutation formula: P(n, r) = n! / (n - r)!
    return math.factorial(n) // math.factorial(n - r)

# Example usage:
n = 5  # Total items
r = 2  # Items to arrange

# Calculate Permutation P(n, r)
P = permutation(n, r)
print(f"Permutation P({n}, {r}) = {P}")


#math is a module in python which is used to perform mathematical operations
import math

# function is create one function that function name is combination
#and pass the parameters n,r
def combination(n, r):
    # Using the combination formula: C(n, r) = n! / (r! * (n - r)!)
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Example usage:
n = 5  # Total items
r = 2  # Items to select

# Calculate Combination C(n, r)
C = combination(n, r)
print(f"Combination C({n}, {r}) = {C}")
