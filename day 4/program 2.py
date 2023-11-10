# Input the year
year = int(input("Enter a year: "))

# Check if the year is a century year or not
if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
