"""
CPT Kyle Yoder
lab3A Mad Libs
06 Sept 2018
"""
"""
Adhere to PEP8 (Comments, formatting, style, etc)
Create a handfull of pharses that require different numbers of inputs
Prompt the user for input(s):
    Inputs can be done a number of ways... 
        (SIMPLE) Ask user for input directly, tell them if the word(s) need to be a verb, noun, etc. 
        (Moderate) Give the user a handful of choices per input to choose from.You will need to create a bank of verbs, nouns, etc for this. 
        (Harder) Give the user cards based off the actual game. Allowing them to draw, etc following the rules. Allow them to only input those cards. 
    (opitional) Implement basic user input checking:
        Check to ensure words are words, numbers are numbers (there are many ways to do this)
        Ensure symobls aren't used if they are not needed
        Check length
        etc
        Implement re-input if input is incorrect
Output the user inputs into the given pharse
Use formatting to not only output the user inputs, but to create a UI within the terminal. Space out certain UI elements such as title of program, choices, menu deceration, etc. 
"""

def readNoun_input():
    capture = raw_input("Please enter a noun: ")
    if(len(capture)<8):
        return capture
    else:
        print "Thats to long"
        capture = readNoun_input()
    return capture

def testLetters(var):
    bad=False
    capture=raw_input(var)
    for i in capture:
        if (ord(i)>=65 and ord(i)<=90):
            bad=False
        elif (ord(i)>=97 and ord(i) <= 122):
            bad=False
        else:
            print "Letters only please"
            capture=testLetters(var)
    return capture

def readInt_input():
    capture = raw_input("Please enter a number: ")
    try:
        capture = int(capture)
    except ValueError:
       print "Please enter a number: "
       capture = readInt_input()
    return capture

def printTitle():
    print '{:_>70}'.format('')
    print ("{:^70}".format("GET READY FOR THE MADNESS"))
    print ("{:_>70}".format(''))
    print '\n\n'


printTitle()



animal=testLetters("Enter an animal ending in an s: ")

vehicle=testLetters("enter a vehicle: ")
print "I'm tired of these mother**** {} on this mother**** {}".format(animal,vehicle)

noun=testLetters("Enter a noun: ")
noun2=testLetters("Enter another noun: ")
verb = testLetters("Enter a verb ending in 'ing': ")
verb2=testLetters("Enter another verb: ")
print "Hell, I'll kill a {} in a {} fight, of if i think he's gonna start a {} fight, or if he {} me, or if there's a woman, or if I'm getting {}; mostly only when I'm getting {}.".format(noun,noun2,noun2,verb,verb2,verb2)
print

name=testLetters("Enter a name: ")
vehicle2=testLetters("enter a vehicle: ")
print "{}yyyyyyy get to the {}".format(name,vehicle2)










"""

madLibDeck={}
madLibDeck[0]="This is the first sentece"
madLibDeck[1]="The second one!"
madLibDeck[2]="I need to have another"
madLibDeck[3]="I'm tired of these"

deck2={}
deck2[0]={"The first half", "the second half"}


counter=0
for i in madLibDeck:
    print ("{} {:_<15}".format(madLibDeck[i],""))
    counter=(len(madLibDeck[i]))
    for j in range(counter):
        print "",
    response=readNoun_input()
    print ("{} {}".format(madLibDeck[i],response))

for k in deck2:
    for j in deck2[k]:
        print ("{} {:_<15}".format(j,"")),
"""