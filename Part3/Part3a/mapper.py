#!/usr/bin/env python
import sys
import re
pattern = re.compile(r'Tags="&lt;(.+)&gt;')
for line in sys.stdin:
    matches = pattern.finditer(line)
    for match in matches:
        data = match.group(1)
        li = data.split('&gt;&lt;')
        for tag in li:
            print("{}\t{}".format(tag, 1))


