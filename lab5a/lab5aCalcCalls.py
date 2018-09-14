
import lab5aFunctions as tm

def readInt_input():
    capture = raw_input("Please enter a number ")
    try:
        capture = int(capture)
    except ValueError:
       print "Please enter a number: "
       capture = readInt_input()
    return capture


def calcLoop(menu):
    if menu==0:
        return 1
    elif menu==1:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} + {} =".format(x,y),
        print tm.add(x,y)
        print"----------------------------------------------"
        return 0
    elif menu==2:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} - {} =".format(x,y),
        print tm.subtract(x,y)
        print"----------------------------------------------"
        return 0
    elif menu ==3:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} * {} =".format(x,y),
        print tm.multiply(x,y)
        print"----------------------------------------------"
        return 0
    elif menu==4:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} / {} =".format(x,y),
        print tm.divide(x,y)
        print"----------------------------------------------"
        return 0
    elif menu==5:
        print"----------------------------------------------"
        x = readInt_input()
        y = readInt_input()
        print "{} to {} power =".format(x,y),
        print tm.power(x,y)
        print"----------------------------------------------"
        return 0
    elif menu==6:
        print"----------------------------------------------"
        print tm.fibonacci()
        print"----------------------------------------------"
        return 0
    elif menu ==7:
        print"----------------------------------------------"
        print tm.squareRoot()
        print"----------------------------------------------"
        return 0