#!/usr/bin/env python3
# print lower_case alpha except q and e
result = ""
for i in range(97, 123):
    if i != 113 and i != 101:
        result = result + chr(i)
print(result)
