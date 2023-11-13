def sum_of_digits(n):
    # Convert the number to a string and iterate through its digits
    # Summing the individual digits
    digit_sum = sum(int(digit) for digit in str(n))
    print("Sum of digits:", digit_sum)

# Accept a positive integer as input
num = int(input("Enter a positive integer: "))

# Call the function to calculate and print the sum of digits
sum_of_digits(num)
