def print_factors(n):
    # Iterate from 1 to n and print factors
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

# Accept a positive integer n as input
num_factors = int(input("Enter a positive integer n: "))

# Call the function to print all factors of n
print_factors(num_factors)
