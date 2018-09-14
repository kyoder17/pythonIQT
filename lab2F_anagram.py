"""
CPT Kyle Yoder
lab2e count words 
05 Sept 2018
"""

#this will get the first string
var1Org=raw_input("Enter your first string \n")
#this will get the second string
var2Org=raw_input("Enter a string to compare it to \n")
#declare lists to use later
myList1=[]
myList2=[]

#antoher variable is used for each to allow for printing of original while removing spaces and lowercase the working copies
var1=var1Org.replace(" ","").lower()
var2=var2Org.replace(" ","").lower()
#write the first string into a list letter by letter
for i in var1:
    myList1.append(i)
#write the second string into another list letter by letter
for i in var2:
    myList2.append(i)

#for each letter in the first list try and remove it from the second    
for i in myList1:
    if i in myList2:
        myList2.remove(i)

#if all letters are removed from the second list then the two words are anagrams        
if len(myList2)==0:
    print "{} and {} are anagrams".format(var1Org,var2Org)
else:
    print "{} and {} are not anagrams".format(var1Org,var2Org)