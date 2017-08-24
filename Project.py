import collections
import os
import LCS
import sys
import time
import datetime
"""
 replaces the string with empty character if any symbol is occured except '_'
    :param line: string
    :return: replaced string
"""
def _string_replace(string):
	for sp in "!@#$%^&*()[]{};:,./<>?\|`~-=+":
		if sp in string :
			string=string.replace(sp,'')
	return string

"""
 Counts the frquency of each words in a given string
    :param line: A line
    :return: frequency of words in a dictionary
"""
def words_count(string):
	frequency_words={}
	string=_string_replace(string)
	li=string.split()
	for word in li:
		if word in frequency_words:
			frequency_words[word]+=1
		else:
			frequency_words[word]=1
	frequency_words=collections.OrderedDict(sorted(frequency_words.items()))
	return frequency_words
"""
 calculates the cross product of words in a dictionary
    :param line: A Dictionary
    :return: integer value of cross product
"""
def product(list):
	product_sum=0
	for values in list.values():
		#print (type(values))
		product_sum=product_sum+((values)**2)
	#print(product_sum)
	return product_sum
"""
 Evaluates the Eclidean norm between two files 
    :param line: A Dictionary
    :return: formulated value as float 
"""
def Euclidean_norm(list1,list2):
	sum_dot_product=0
	for word in list1.keys():
		if word in list2:
			dot_product=list1[word]*list2[word]
			sum_dot_product=sum_dot_product+dot_product
	#print (sum_dot_product)
	cross_product=(product(list1)*product(list2))**(1/2)
	#print (cross_product)
	try:
		cos_teta= (sum_dot_product/cross_product)*100
	#print (cos_teta)
		return cos_teta
	except ZeroDivisionError:
		return 0		
"""
 Prints the matrix in readble format
    :param line: A matrix(list of lists)
    :return: nothing
"""
def _print_matrix_(matrix):
	print (end=" "*len(max(files, key=len)))
	mx = max((len(str(ele)) for sub in matrix for ele in sub))
	for row in matrix:
		print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
	return 0
old_stdout = sys.stdout
log_file = open("message.log","a+")
sys.stdout = log_file
files=[]
bag_of_words=[files]
longest_sequence_substring=[files]
for file in os.listdir('.'):
     if (os.path.isfile(file)) and (file.endswith(".txt") and file!='message.txt'):
     	files.append(file)
for each_file1 in files:
	li=[each_file1]
	li_lcs=[each_file1]
	for each_file2 in files:
		if each_file1!=each_file2:
			file1=open(each_file1,'r')
			file2 = open(each_file2,'r')
			file1_string=file1.read()
			file2_string=file2.read()
			word_list1=(words_count(file1_string))
			word_list2=(words_count(file2_string))
			li.append(round((Euclidean_norm(word_list1,word_list2)),2))
			li_lcs.append((LCS.longestSubstringFinder(file1_string,file2_string)))
		else:
			li.append('X')
			li_lcs.append('X')
	bag_of_words.append(li)
	longest_sequence_substring.append(li_lcs)
#print (longest_sequence_substring)
print ('Executed on : '+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
print ("*********Bag of words********")
_print_matrix_(bag_of_words)
print ("*********Longest Sequence Substring********") 
_print_matrix_(longest_sequence_substring)
print('---------------------------------------------------------------------------------')
sys.stdout = old_stdout

log_file.close()