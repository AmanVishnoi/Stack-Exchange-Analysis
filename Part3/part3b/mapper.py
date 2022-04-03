#!/usr/bin/env python
import sys
import re
view_count = re.compile(r'ViewCount="(\d+)"')
title = re.compile(r'Title="(.+)" Tags')
for line in sys.stdin:
    view_count_no = view_count.search(line)
    title_of_post = title.search(line)
    try:
        print("{}\t{}".format(view_count_no.group(1), title_of_post.group(1)))
    except AttributeError:
        continue



