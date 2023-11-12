Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_time_of_day(hour):
    if 0 <= hour <= 5:
        return "NIGHT"
    elif 6 <= hour <= 11:
        return "MORNING"
    elif 12 <= hour <= 17:
        return "AFTERNOON"
    elif 18 <= hour <= 23:
        return "EVENING"
    else:
        return "INVALID"

# Input
hour = int(input())

# Get and print the time of the day
time_of_day = get_time_of_day(hour)
print(time_of_day)