def print_first_n_integers(n):
    # Use range to generate the first n integers and join them with commas
    result = ', '.join(str(i) for i in range(1, n+1))
    print(result)

# Accept a positive integer n as input
num_n = int(input("Enter a positive integer n: "))

# Call the function to print the first n integers
print_first_n_integers(num_n)
