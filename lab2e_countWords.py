"""
CPT Kyle Yoder
lab2e count words 
05 Sept 2018
"""


userInput=raw_input("please enter your string ")

list1=userInput.split(" ")
total=len(list1)
print "The number of words you entered is {}".format(total)


print "These words contained a total of {} letters".format(len(userInput))


char = raw_input("Enter a letter you would like to count in your string: ")
count = 0
for c in userInput:
    if char == c:
      count += 1

print "There are {} instances of {} in your string".format(count,char)

counter1 =0
counter2 =0

for i in userInput:
    if(i.islower()):
        counter1 += 1
    elif(i.isupper()):
        counter2 +=1
print "The number of lowercase letters is {}".format(counter1)
print "The number of uppercase letters is {}".format(counter2)


