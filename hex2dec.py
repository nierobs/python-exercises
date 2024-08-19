#!/usr/bin/python3
import sys
letters = { "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15 }
for val in sys.argv[1:]:
    result = 0
    for i in range(len(val)):
        num = val[::-1][i]
        if num in letters:
            result += letters[num] * 16 ** i
        else:
            result += int(num) * 16 ** i
    print(result, end = " ")
print()
