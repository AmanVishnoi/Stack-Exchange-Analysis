# Stack Exchange Analysis using hadoop
## I have divided the entire project into 5 parts for the sake of simiplicity
### The dataset for the same is avialable at datascience.stackexchange at this [link](https://archive.org/download/stackexchange/datascience.stackexchange.com.7z)
1-Creating a schema of the dataset for all the files that are provided in the folder

2-Counting the number of badges and user's per badge in the Badges.xml file by making a shell script that will run in parellel using hadoop streaming so as to get more insights into the data

3-Using the post.xml file we analyze the following
    
	- Analyzing the popularity of rags(how many posts used each tag). The graph that I have got is
	![Tag Popularity vs Posts Used](https://github.com/AmanVishnoi/Stack-Exchange-Analysis/blob/main/Part3/Part3a/TagsPopularity.jpeg)
    
	- Calculating the View Count distribution(how many posts were viewed a given number of times). Also fetching the top 10 posts on data stack exchange. The graph that I have obtained is 
	

	![Post vs View Count](https://github.com/AmanVishnoi/Stack-Exchange-Analysis/blob/main/Part3/Part3b/ViewCount.jpeg)
    
	- To understand how servers of stack exchange were used in an efficient manner i calculated posts per Hour of the day to understand when the data were most busy.To get insights I draw graph for Activity per hour vs hour of day	
	
	
	![Activity Per Hour vs Hour of the Day](https://github.com/AmanVishnoi/Stack-Exchange-Analysis/blob/main/Part3/Part3c/Activity.jpeg)

4-Using the comments.xml file we create summary table for the total Number of Comments and median of Comment Length by Month from May 2014 to Sep 2021. To get the length of comments i plotted Number of comments by Month
	
![Comments vs Months](https://github.com/AmanVishnoi/Stack-Exchange-Analysis/blob/main/Part4/Comments.jpeg)

5-I have User.xml file and PostHistory.xml, we calculated the correlation coefficient of user in Users.xml to total answers given by the use in PostsHistory.xml file
