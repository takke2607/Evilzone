
#This the code to solve the challenge of the evilzone.org
# Author : Rohan Takke
# github : https://github.com/takke2607
# Instagram : https://www.instagram.com/rohantakke
# Twitter : https://twitter.com/takkerohan97
#
import hashlib 
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://evilzone.org/challenges/fast_hasher/') 				#calling the web url
hash_button = driver.find_element_by_tag_name('button') 				#finding the element in the html
#print hash_button 														#getting element id
hash_button.click() 													#clicking the button
textarea = driver.find_element_by_tag_name('textarea')					#finding the text element
hashes = textarea.get_attribute('value')
#print ("This are hashes")
#print hashes
#print ("*******************************************************************")
hash_list = hashes.split()                                               #appending all the gathered hashes in list
hash_hash = []															 	
for hashes in hash_list:
	string = hashes
	temp = hashlib.md5(string).hexdigest()
	hash_hash.append(temp)												#appending the hash of hashes in the new list
#print ("This are hashed hashes")										    	 
#print hash_hash	
res = ''
for ele in hash_hash: 
	res += ele													#concatenating all the hashes

#print ("*******************************************************************")	
#print("This is the concatenated hash")
#print res
#print ("*******************************************************************")	
final = hashlib.md5(res).hexdigest()
print("This is your final hash, copy and paste it in the '''check answer''' section!")
print final
