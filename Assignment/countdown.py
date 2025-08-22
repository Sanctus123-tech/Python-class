# Countdown from 10 to 1

import time   # To create delay

for i in range(10, 0, -1):   # Start at 10, stop at 1
    print(i)
    time.sleep(1)   # Wait 1 second between numbers

print("BOOM!!! ")
