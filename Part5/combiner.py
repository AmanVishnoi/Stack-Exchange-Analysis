#!/usr/bin/env python
import sys

# Two types of output possible : UserId Reputation number  ########## UserId Answer 1

USER_ID = None
REPUTATION = None
TOTAL_ANSWERS = 0


sumX = 0
sumY = 0
sumXY = 0
sumXSqr = 0
sumYSqr = 0
n = 0


for line in sys.stdin:
    temp = line.split("\t")
    user_id = temp[0]
    word = temp[1]
    count = int(temp[2])

    if user_id == USER_ID:
        if word == "Reputation":
            REPUTATION = count
        else:
            TOTAL_ANSWERS += 1

    else:
        if USER_ID:
            sumX += REPUTATION
            sumY += TOTAL_ANSWERS
            sumXY += REPUTATION * TOTAL_ANSWERS
            sumXSqr += REPUTATION * REPUTATION
            sumYSqr += TOTAL_ANSWERS * TOTAL_ANSWERS
            n += 1
        if word == "Reputation":
            REPUTATION = count
            TOTAL_ANSWERS = 0
        else:
            TOTAL_ANSWERS = 1
            REPUTATION = None
        USER_ID = user_id

sumX += REPUTATION
sumY += TOTAL_ANSWERS
sumXY += REPUTATION * TOTAL_ANSWERS
sumXSqr += REPUTATION * REPUTATION
sumYSqr += TOTAL_ANSWERS * TOTAL_ANSWERS
n += 1

print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format("key", sumX, sumY, sumXY, sumXSqr, sumYSqr, n))


