"""
CPT Kyle Yoder
Lab3F Fizz Buzz
10 Sept 2018
"""

"""
this is 72 i long for pep8 testing
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
Iterate through a loop 100 times 
printing Fizz for any number divisable by 3 
and Buzz for any number divisable by 5. 
If the number is divisable by both print FizzBuzz.
 All other numbers print the number.
Adhere to PEP8 (Comments, formatting, style, etc)
Utilize proper formatting
Utilize proper and clean loops and conditionals
Follow instructions above

Create two versions:
One version which is as short as possible
Another version which is as drawn out and creative as possible
"""
#round 1
#loop through
for i in range(100):
    #check for mod 3 and mod 5
    if ((i%5==0) and (i%3==0)):
        #if mod for both print FizzBuzz
        print "FizzBuzz"
    #else check mod 3 and print Fizz
    elif (i%3==0):
        print "Fizz"
    #else check mod 5 and print Buzz
    elif (i%5==0):
        print "Buzz"
    #else print i
    else:    
        print i

#round 2
#complex way
#create a list of each mod value 
fiveList=[]
threeList=[]

for k in range(0,21):
    fiveList.append(k*5)
for l in range(0,34):
    threeList.append(l*3)
#print fiveList    
#print threeList
j=1
#loop through
while(j%100!=0):
    #if in both list print FizzBuzz
    if j in threeList and j in fiveList:
        print "FizzBuzz"
    #if in list for divisable by 3 print Fizz
    elif j in threeList:
        print "Fizz"
    #if in list for divisable by 5 print Buzz
    elif j in fiveList:
        print "Buzz"
    #else print the loop counter
    else:
        print j
    j+=1
    


"""
#round3
#from Graham, the real best way to do this, 
# great example to save for later use
counter=100
#sets the loop size
for i in range(1, counter + 1):
    #loops through and prints fizz if mod three, 
    # then without a space prints buzz if mod 5
    #or prints the count
    print 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i


#another example form Graham
#done in one line broken up for pep8 
#checks each thing in order and only prints if true

for i in range(1, counter + 1):

     print (
         i if (i % 3 != 0 and i % 5 != 0) 
         else ("FizzBuzz" if (i % 3 == 0 and i % 5 == 0) 
         else ("Fizz" if (i % 3 == 0) else "Buzz"))
     )
"""