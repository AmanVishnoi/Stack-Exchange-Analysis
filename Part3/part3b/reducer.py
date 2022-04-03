#!/usr/bin/env python
import sys

no_of_posts = 0
current_view_count = None
post_title = ""
most_viewed_posts = {}
dic_length = 0

for line in sys.stdin:
    temp = line.split("\t")
    view_count = int(temp[0])
    title = temp[1]

    if current_view_count == view_count:
        no_of_posts += 1
    else:
        if current_view_count:
            print("{}\t{}".format(current_view_count, no_of_posts))
        # By analysing the data tells me that most viewed post are often single
        if dic_length < 10:
            most_viewed_posts[title] = view_count
            dic_length += 1
        else:
            min_count = min(most_viewed_posts.values())
            if current_view_count > min_count:
                del most_viewed_posts[min(most_viewed_posts, key=most_viewed_posts.get)]
                most_viewed_posts[post_title] = current_view_count 
        current_view_count = view_count
        no_of_posts = 1
        post_title = title

print("{}\t{}".format(current_view_count, no_of_posts))
del most_viewed_posts[min(most_viewed_posts, key=most_viewed_posts.get)]
most_viewed_posts[post_title] = current_view_count 
print("\n\nTop 10 Most Viewed Posts")
top_10_most_viewed_posts = most_viewed_posts.keys()
for post in top_10_most_viewed_posts:
    print(post)

