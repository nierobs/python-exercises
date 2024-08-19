#!/usr/bin/python3
import sys
for val in sys.argv[1:]:
    result = 0
    for i in range(len(val)):
        result += int(val[::-1][i]) * 8 ** i
    print(result, end = " ")
print()
