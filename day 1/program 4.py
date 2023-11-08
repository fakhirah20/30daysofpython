# Input temperature in degrees Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Print the result
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")
