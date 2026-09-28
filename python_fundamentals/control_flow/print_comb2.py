#!/usr/bin/env python3
# Print num from 0 to 99 formatted as two-digit num
for i in range(0, 100):
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
