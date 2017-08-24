import collections
import os
import LCS

def words_count(string):
	frequency_words={}
	string = string.replace("!@#$%^&*()[]{};:,./<>?\|`~-=+", "")
	li=string.split()
	for word in li:
		if word in frequency_words:
			frequency_words[word]+=1
		else:
			frequency_words[word]=1
	frequency_words=collections.OrderedDict(sorted(frequency_words.items()))
	return frequency_words
def product(list):
	product_sum=0
	for values in list.values():
		#print (type(values))
		product_sum=product_sum+((values)**2)
	#print(product_sum)
	return product_sum
def Euclidean_norm(list1,list2):
	sum_dot_product=0
	for word in list1.keys():
		if word in list2:
			dot_product=list1[word]*list2[word]
			sum_dot_product=sum_dot_product+dot_product
	#print (sum_dot_product)
	cross_product=(product(list1)*product(list2))**(1/2)
	#print (cross_product)
	cos_teta= (sum_dot_product/cross_product)*100
	#print (cos_teta)
	return cos_teta		

files=[]

bag_of_words=[]
longest_sequence_substring=[]
for file in os.listdir('.'):
     if (os.path.isfile(file)) and (file.endswith(".txt")):
     	files.append(file)
for each_file1 in files:
	li=[]
	li_lcs=[]
	for each_file2 in files:
		if each_file1!=each_file2:
			file1=open(each_file1,'r')
			file2 = open(each_file2,'r')
			file1_string=file1.read()
			file2_string=file2.read()

			word_list1=(words_count(file1_string))
			word_list2=(words_count(file2_string))
			#print(file1_string)
			#print(file2_string)
			li.append(round((Euclidean_norm(word_list1,word_list2)),2))
			li_lcs.append((LCS.longestSubstringFinder(file1_string,file2_string)))
			#print(longest_sequence)
		else:
			li.append(0)
			li_lcs.append(0)
	bag_of_words.append(li)
	longest_sequence_substring.append(li_lcs)

print ("*********Bag of words********") 		
for i in bag_of_words:
	print (i)

#print(bag_of_words)
print ("*********Longest Sequence Substring********") 
for i in longest_sequence_substring:
	print (i)

#print (longest_sequence_substring)
#print (max(li_lcs))


