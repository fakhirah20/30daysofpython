def sum_divisible_by_a_and_b(a, b):
    # Initialize sum to 0
    total_sum = 0

    # Iterate through the range [1000, 2001) and add numbers divisible by both a and b
    for num in range(1000, 2001):
        if num % a == 0 and num % b == 0:
            total_sum += num

    # Print the result or 0 if no numbers satisfy the condition
    if total_sum != 0:
        print("Sum of numbers divisible by both {} and {} in [1000, 2000]: {}".format(a, b, total_sum))
    else:
        print("No numbers satisfy the condition in the given range.")

# Accept two positive integers a and b as input
num_a = int(input("Enter a positive integer a: "))
num_b = int(input("Enter a positive integer b: "))

# Call the function to calculate and print the sum of numbers in the range [1000, 2000] divisible by both a and b
sum_divisible_by_a_and_b(num_a, num_b)
