"""
CPT Klye Yoder
Lab3d factorial
07 Sept 2018
"""

#get user input
userInput=raw_input("Please enter an integer: ")
#use a while loop to check if it is an int
x=0
while(x==0):
    try:
        userInput=int(userInput)
        x=1
    except ValueError:
        userInput=raw_input("Please enter an integer: ")
#set up factorial
outPut=1
i=int(1)
#while loop through factorial multiplying for each number
while(i < (userInput+1)):
    outPut=outPut*i
    i+=1
#print the output
print outPut