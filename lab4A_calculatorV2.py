"""
CPT Kyle Yoder
Lab4A calculator version 2
10 Sept 2018
"""


userInput=raw_input("enter input ")
operatorList=['+','-','*','/']

#lambda expression for additon
def add(x,y):
     result=lambda x,y: x+y
     return result(x,y)

#lambda expression for subtraction
def subtract(x,y):
     result=lambda x,y: x-y
     return result(x,y)

#lambda expression for multiplication
def multiply(x,y):
     result=lambda x,y: x*y
     return result(x,y)

#lambda expression for division
def divide(x,y):
     result=lambda x,y: x/y
     return result(x,y)

#lambda expression for rasing a number to a power
def power(x,y):
     result=lambda x,y: x**y
     return result(x,y)



def operations(current,i,next):
    if i=='+':
        return add(current,next)


var=''       
start=0
end=0
current=0
for i in userInput:
    if i in operatorList:
        var=userInput[start:end]
        print var
        start=end+1
        end=end+1
        var=int(var)
        print var
        current=operations(current,i,var)
        print current
    elif end==(len(userInput)-1):
        end+=1
        var=userInput[start:end]
        print var
    else:
        end+=1


