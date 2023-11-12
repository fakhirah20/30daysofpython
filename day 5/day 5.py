Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_fair_division(n, share1, share2, share3):
    # Check if all shares are non-zero
    if share1 == 0 or share2 == 0 or share3 == 0:
        return "UNFAIR"

    # Check if no two shares are the same
    if share1 == share2 or share1 == share3 or share2 == share3:
        return "UNFAIR"

    # Check if the sum of shares equals the total number of coins
    if share1 + share2 + share3 != n:
        return "UNFAIR"

    return "FAIR"

# Input
n = int(input())
share1 = int(input())
share2 = int(input())
share3 = int(input())

# Check and print the result
result = is_fair_division(n, share1, share2, share3)
print(result)
