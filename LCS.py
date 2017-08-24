import numpy
"""
 Finds the longest substring from two strings
    :param line: two strings
    :return: formulated value of the longest string
"""
def longestSubstringFinder(file_string1, file_string2):
	answer = ""

	if len(file_string1) == len(file_string2):
	    if file_string1==file_string2:
	        return file_string1
	    else:
	        longer=file_string1
	        shorter=file_string2
	elif (len(file_string1) == 0 or len(file_string2) == 0):
	    return ""
	elif len(file_string1)>len(file_string2):
	    longer=file_string1
	    shorter=file_string2
	else:
	    longer=file_string2
	    shorter=file_string1

	lcs_matrix = numpy.zeros((len(shorter), len(longer)))
	#print (lcs_matrix)
	for i in range(len(shorter)):
	    for j in range(len(longer)):               
	        if shorter[i]== longer[j]:
	            lcs_matrix[i][j]=1

	longest=0

	start=[-1,-1]
	end=[-1,-1]    
	for i in range(len(shorter)-1, -1, -1):
	    for j in range(len(longer)):
	        count=0
	        begin = [i,j]
	        while lcs_matrix[i][j]==1:

	            finish=[i,j]
	            count=count+1 
	            if j==len(longer)-1 or i==len(shorter)-1:
	                break
	            else:
	                j=j+1
	                i=i+1

	        i = i-count
	        if count>longest:
	            longest=count
	            start=begin
	            end=finish
	            break

	answer=shorter[int(start[0]): int(end[0])+1]
	#print (answer)
	return round((((len(answer)*2)/((len(file_string1))+(len(file_string2))))*100),2)

"""str1="what is your name"
str2="my name is xyz"
print (longestSubstringFinder(str1,str2))"""