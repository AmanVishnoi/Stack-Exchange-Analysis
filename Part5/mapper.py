#!/usr/bin/env python
import sys
import re

reputation_users = re.compile(r'Reputation="(\d+)"')
user_id_users = re.compile(r'Id="(\d+)"')
postHistoryTypeId_postHistory = re.compile(r'PostHistoryTypeId="(\d+)"')
user_id_postHistory = re.compile(r'UserId="(\d+)"')


for line in sys.stdin:
    PostID = postHistoryTypeId_postHistory.search(line)
    if PostID:
        if int(PostID.group(1)) == 2:
            User_ID = user_id_postHistory.search(line)
            try:
                print("{}\t{}\t{}".format(User_ID.group(1), "Answer", 1))
            except AttributeError:
                continue
    else:
        Reputation = reputation_users.search(line)
        User_ID = user_id_users.search(line)
        try:
            print("{}\t{}\t{}".format(User_ID.group(1), "Reputation", Reputation.group(1)))
        except AttributeError:
            continue
