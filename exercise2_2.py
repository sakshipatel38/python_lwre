import time

timestamp = time.strftime("%H:%M:%S")
print("current time is:", timestamp)
if "00:00:00" <= timestamp < "12:00:00":
    print("good morning")
elif "12:00:00" <= timestamp < "18:00:00":
    print("good afternoon")
elif "18:00:00" <= timestamp < "21:00:00":
    print("good evening")
elif "21:00:00" <= timestamp <= "23:59:59":
    print("good night")
else:
    print("invalid time")

# here we had used time module to get current time and based on that time we are giving output

# also this is automatic way of taking time input from system

'''The strftime() function is used to format time/date objects into readable strings using a format pattern. In Python, it’s available via the time module (and also in datetime).'''

'''| Code | Meaning         | Example                  |
| ---- | ------------------ | ------------------------ |
| `%Y` | Year (4 digits)    | 2025                     |
| `%y` | Year (2 digits)    | 25                       |
| `%m` | Month (01–12)      | 12                       |
| `%d` | Day (01–31)        | 24                       |
| `%H` | Hour (00–23)       | 17                       |
| `%I` | Hour (01–12)       | 05                       |
| `%M` | Minute (00–59)     | 07                       |
| `%S` | Second (00–59)     | 45                       |
| `%p` | AM/PM              | PM                       |
| `%a` | Weekday (short)    | Wed                      |
| `%A` | Weekday (full)     | Wednesday                |
| `%b` | Month (short)      | Dec                      |
| `%B` | Month (full)       | December                 |
| `%c` | Locale date & time | Wed Dec 24 17:00:12 2025 |
| `%x` | Locale date        | 12/24/25                 |
| `%X` | Locale time        | 17:00:12                 |
'''