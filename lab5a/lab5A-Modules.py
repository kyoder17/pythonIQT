"""
CPT Kyle Yoder
lab5A modules
12 Sept 2018
"""
import lab5aFunctions
import lab5aCalcCalls as theLoop

#will check input to ensure it is an integer
def readInt_input():
    capture = raw_input("Please enter a number ")
    try:
        capture = int(capture)
    except ValueError:
       print "Please enter a number: "
       capture = readInt_input()
    return capture

    
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



if __name__ == '__main__':
    while (True):
        menu= menuSelection()
        check=theLoop.calcLoop(menu)
        if check==1:
            break