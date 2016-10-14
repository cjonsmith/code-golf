# Sum the list that is the sum of an original lists neighbors in place. 
# Source: http://codegolf.stackexchange.com/questions/96188/sum-of-neighbours
# 50 bytes.
lambda x:sum(map(sum,zip(x,x[1:]+[0],[0]+x[:-1])))