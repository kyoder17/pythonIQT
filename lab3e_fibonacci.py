"""
CPT Klye Yoder
Lab3e Fibonacci
07 Sept 2018
"""


def fib(c):
    if c<=1:
        return c
    else:
        return fib(c-1)+fib(c-2)
        

n=raw_input("Enter a number for Fibonacci ")
while(True):
    try:
        n=int(n)
        break
    except ValueError:
        n=raw_input("Please enter an integer: ")
     
print "\nIterative"  
a=0
b=1
if n==0:
    print n
elif n==1:
    print n
else:
    print 0
    print 1
    for i in range(n-1):
        temp=a+b
        a=b
        b=temp       
        print temp

print "\nRecursive"
while(True):
    for i in range(n+1):
        print(fib(i))
    break





