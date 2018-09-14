"""
CPT Kyle Yoder
lab2d strings
05 Sept 2018
"""


userInput=raw_input("please enter your string ")
print "here is the string you entered "
print userInput

newString=userInput[::-1]
print "And here it is reversed "
print newString
newString=newString.upper()
print "And here it is revered and capitalized"
print newString

print raw_input("Tell me something good")[::-1].upper()