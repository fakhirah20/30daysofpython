# Input two variables
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Swap the values without a third variable
a = a + b
b = a - b
a = a - b

# Print the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
