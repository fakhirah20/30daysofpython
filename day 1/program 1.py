def count_digits(number):
    return len(str(number))

# Input two positive integers
x = int(input("Enter a positive integer x: "))
y = int(input("Enter a positive integer y: "))

# Calculate x^y
result = x ** y

# Calculate the number of digits in x^y
num_digits = count_digits(result)

# Print the result
print(f"{x}^{y} = {result}")
print(f"Number of digits in {x}^{y}: {num_digits}")
