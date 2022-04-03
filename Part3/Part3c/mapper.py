#!/usr/bin/env python
import sys
import re
CreationDate = re.compile(r'CreationDate="(\d{4})-(\d{2})-(\d{2})T(\d{2}):\d{2}:\d{2}')

for line in sys.stdin:
    matches = CreationDate.search(line)
    try:
        s = f"hour {matches.group(4)}"
        print("{}\t{}".format(s, 1))
    except AttributeError:
        continue
