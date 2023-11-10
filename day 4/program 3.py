import math

# Input coefficients of the quadratic equation
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))

# Calculate the discriminant
discriminant = b**2 - 4 * a * c

# Check the nature of the roots
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots of the quadratic equation are real and distinct: {root1} and {root2}")
elif discriminant == 0:
    # One real and repeated root
    root = -b / (2 * a)
    print(f"The root of the quadratic equation is real and repeated: {root}")
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print(f"The roots of the quadratic equation are complex: {root1} and {root2}")
