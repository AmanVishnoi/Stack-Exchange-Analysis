#!/usr/bin/env python
import sys

current_date = None
current_count = None

for line in sys.stdin:
    temp = line.split("\t")
    date = temp[0]
    count = temp[1]
    try:
        count = int(count)
    except ValueError:
        continue

    if current_date == date:
        current_count += 1
    else:
        if current_date:
            print("{}\t{}".format(current_date, current_count))
        current_date = date
        current_count = 1

print("{}\t{}".format(current_date, current_count))

