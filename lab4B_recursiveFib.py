"""
CPT Kyle Yoder
Lab4B Recursive Fibonacci
10 Sept 2018
"""

#this is the recusive function that calls itself
def fib(c):
    if c<=1:
        return c
    else:
        return fib(c-1)+fib(c-2)

#will run n number of times, stay under 30 for time       
n=15
print "\nRecursive"
while(True):
    for i in range(n+1):
        print(fib(i))
    break