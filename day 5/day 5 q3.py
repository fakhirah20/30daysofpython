Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_meeting_possible(employees):
    # Check if the sum of employee-ids of every pair of adjacent employees is even
    for i in range(5):
        if (employees[i] + employees[(i + 1) % 5]) % 2 != 0:
            return "NO"
    return "YES"

# Input
employees = [int(input()) for _ in range(5)]

# Check and print the result
result = is_meeting_possible(employees)
print(result)