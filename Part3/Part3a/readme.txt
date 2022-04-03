Summary Table
mapper-
	Extract the tags from the each_row tag passed through input stream file and emit 	(tag_name,1) for each tag.

map(OwnerUserId,CreationDate,PostTypeId,Tags,Score,ViewCount,AnswerCount,Body,LastActivityDate	Title,CommentCount,Favourite Count,Closed Date) ---> (Tag, 1) for each of the tag in Tags

reducer-

reducer(Tag,List[1,1,1,..........]) ---> (Tag, sum(List))





the output folder contains the output of mapreduce and the Tag popularity graph shows that it looks like a unimodal distribution

