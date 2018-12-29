#!/usr/bin/env python3

a = []

for i in range(2000, 3201):
    if i // 7 and (i%5 != 0):
        a.append(str(i))

print(','.join(a))
