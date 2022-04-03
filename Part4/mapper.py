#!/usr/bin/env python
import sys
import re

month = re.compile(r'CreationDate="(\d{4})-(\d{2})-\d{2}T')
comment = re.compile(r'Text="(.+)" CreationDate')
for line in sys.stdin:
    match_month = month.search(line)
    match_comment = comment.search(line)
    try:
        print("{}\t{}".format(f"{match_month.group(1)}-{match_month.group(2)}", len(match_comment.group(1))))
    except AttributeError:
        continue
