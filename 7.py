#!/usr/bin/env python3

inputt = input()
dimensions = [int(x) for x in inputt.split(',')]
row = dimensions[0]
col = dimensions[1]

multilist = [[0 for col in range(col)] for row in range(row)]

for row in range(row):
    for col in range(col):
        multilist[row][col] = row*col

print(multilist)
