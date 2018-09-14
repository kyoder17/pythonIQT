"""
CPT Klye Yoder
Lab3c fun house
07 Sept 2018
"""


def readInt_input():
    capture = raw_input("Chose Door 1, 2, or 3\n")
    try:
        capture = int(capture)
    except ValueError:
       print "Please enter a number: "
       capture = readInt_input()
    return capture

print "Welcome to the Phun House!\n"
choice=readInt_input()
theEnd=0
while theEnd==0:
    print "test"
    if choice ==1:
        print "Oh no this is bad why are there so many clowns"
        choice= raw_input("Chose Door 4, or 2\n")
        choice=int(choice)
        if choice == 4:
            print "How are there even more clowns here"

    elif choice==2:
        print "This room isnt so bad"
        theEnd=1

    elif choice ==3:
        print "Is this all there is here?"
        theEnd=1

    else:
        print "Are you going to just stand there? Go start over"
        choice=0
        if choice ==0:
            choice =raw_input("Chose Door 1, 2, or 3\n")
            choice = int(choice)
    print theEnd
    theEnd=int(theEnd)




