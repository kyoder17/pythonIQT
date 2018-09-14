
import math

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


#print the bonus doge file!!!
dogeFile=open('doge_banner2.txt','r')
data= dogeFile.read()
print data
dogeFile.close

#loop through and execute a function based on menu choice 
#will run until 0 selection