#!/usr/bin/env python
import sys

sumX = 0
sumY = 0
sumXY = 0
sumXSqr = 0
sumYSqr = 0
n = 0
KEY = "key"

for line in sys.stdin:
    temp = line.split()
    if temp[0] == KEY:
        sumX += int(temp[1])
        sumY += int(temp[2])
        sumXY += int(temp[3])
        sumXSqr += int(temp[4])
        sumYSqr += int(temp[5])
        n += int(temp[6])

print("Coefficient of correlation is:")
num = n * sumXY - sumY * sumX
deno_part1 = n * sumXSqr - (sumX ** 2)
deno_part2 = n * sumYSqr - (sumY ** 2)
deno = deno_part2 * deno_part1
Corr = num / (deno ** 0.5)
print(Corr)

    
    
