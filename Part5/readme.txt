mapper-
There are two relations Users.xml and PostHistory.xml 
	map(<row........../>, Reputation)) ------------> (UserId, ("Repuatation", Reputation)) where Reputation indicates that it is from Users.xml
	map(<row........../>, Answers)) --------> (UserId, ("Answers", 1)) where Answers indicate that it is from PostHistory.xml

output from mapper will be of two types --- (UserId, ("Reputation", Reputation)) or (UserId, ("Answer", 1))

reducer---


reducer(UserId,  List[("Reputation", Reputaion),("Answer", 1), ("Answer", 1).............]) ---> (UserId, (Reputation, sum(Answers)))

then i calculated correlation which turns out to be 0.822