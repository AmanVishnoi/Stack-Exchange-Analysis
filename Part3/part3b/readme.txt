mapper-
	map(<row ..... />) ---> (View_Count, Title of post)

reducer-
	reucer(View_Count, List[Title of post, Title of Post.........]) ----> (View_count, len(List)) and (top_10_maximum(List)) based on their view count
	







As the view count increases the number of posts decreases thus graph shows positive skewness. The top 10 most viewed posts are in "out" folder. My mapper and reducer code prints both the view-count vs number of posts and the top 10 most viewed post at the end