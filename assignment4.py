# PROBLEM 1: SQUARE ROOTS
# Solving a quadratic equation using the quadratic formula

# Import the math module in order to use the square root function
import math

# The coefficients of the quadratic equation: ax^2 + bx + c = 0
a = 1
b = -5.86
c = 8.5408

# Calculate the discriminant part of the formula: b^2 - 4ac
discriminant = b**2 - 4 * a * c

# Use the quadratic formula to calculate the two roots
# Root 1 uses the + sign
root1 = (-b + math.sqrt(discriminant)) / (2 * a)

# Root 2 uses the - sign
root2 = (-b - math.sqrt(discriminant)) / (2 * a)

# I am trying out rounding to make the output easier to read
rounded_root1 = round(root1, 2)
rounded_root2 = round(root2, 2)

# Print the results to the screen
print("The roots of the equation are:")
print("Root 1:", rounded_root1)
print("Root 2:", rounded_root2)


# I like to add a few blank lines between problems to see them easier
print('')
print('')


# PROBLEM 2: RECIPROCALS
# Printing reciprocals from 1/2 to 1/10

# I am using a for loop to print the decimal values of 1/2 through 1/10

# Loop through numbers 2 to 10 (inclusive)
for i in range(2, 11):
    # Calculate the reciprocal (1 divided by the number)
    reciprocal = 1 / i

    # Round the result to 3 decimal places for cleaner output
    rounded_reciprocal = round(reciprocal, 3)

    # Print the result
    print(f"1/{i} = {rounded_reciprocal}")

















