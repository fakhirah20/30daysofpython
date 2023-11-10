def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Input temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ").upper()

# Perform conversion based on the input unit
if unit == "C":
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")
elif unit == "F":
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
