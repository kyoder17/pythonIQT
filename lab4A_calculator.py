"""
CPT Kyle Yoder
Lab4A calculator
10 Sept 2018
"""

import math

#will check input to ensure it is an integer
def readInt_input():
    capture = raw_input("Please enter a number ")
    try:
        capture = int(capture)
    except ValueError:
       print "Please enter a number: "
       capture = readInt_input()
    return capture
#checks the menu selection to ensure it is an input
def menu_Input():
    capture = raw_input("Menu Selection: ")
    try:
        capture = int(capture)
    except ValueError:
       print "Please make a selection: "
       capture = readInt_input()
    return capture

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

    
#this is the recusive function that calls itself
def fib(c):
    if c<=1:
        return c
    else:
        return fib(c-1)+fib(c-2)

def fibonacci():
    n=readInt_input()
    print "The factorial of {} is ".format(n)
    #for i in range(n):
    for i in range(n+1):
        print(fib(i))
    return

#use import math to solve for square root
def squareRoot():
    userInput1 = readInt_input()
    print "The square root of {} is ".format(userInput1)
    return math.sqrt(userInput1)


#print the menu
def menuSelection():
    print "Enter 0 to exit"
    print "Enter 1 for additon"
    print "Enter 2 for subtraction"
    print "Enter 3 for multiplication"
    print "Enter 4 for division"
    print "Enter 5 for power"
    print "Enter 6 for fibonacci"
    print "Enter 7 for square root of a number"
    menu=readInt_input()
    return menu


#print the bonus doge file!!!
dogeFile=open('doge_banner2.txt','r')
data= dogeFile.read()
print data
dogeFile.close

#loop through and execute a function based on menu choice 
#will run until 0 selection
while(True):
    menu=menuSelection()
    if menu==0:
        break
    elif menu==1:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} + {} =".format(x,y),
        print add(x,y)
        print"----------------------------------------------"
    elif menu==2:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} - {} =".format(x,y),
        print subtract(x,y)
        print"----------------------------------------------"
    elif menu ==3:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} * {} =".format(x,y),
        print multiply(x,y)
        print"----------------------------------------------"
    elif menu==4:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} / {} =".format(x,y),
        print divide(x,y)
        print"----------------------------------------------"
    elif menu==5:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} to {} power =".format(x,y),
        print power(x,y)
        print"----------------------------------------------"
    elif menu==6:
        print"----------------------------------------------"
        print fibonacci()
        print"----------------------------------------------"
    elif menu ==7:
        print"----------------------------------------------"
        print squareRoot()
        print"----------------------------------------------"
