"""
CPT Klye Yoder
Student Code: Lab3B file in out
06 Sept 2018

Instructions:
* You are provided with a text file that contains the best song lyrics in the world
    * Problem is... the song lyrics are encrypted with a simple XOR.
* You will need to decrypt the lyrics
    * The key is 27
    * You have been provided with a decent chunk of the code with conditionals and loops already created...
    * Feel free to create yours from scratch if you want a greater challange. 
* You will need to think outside the box. Remember what XOR is, the type of data it acts on, how much data, etc. 
"""

def studentCode():
    # TODO: Create variables and open file here
    key = 27
    finalString = ""
    file = open("file.txt",'r')
    # TODO: Read your file entirely into tempString
    tempString=file.read()

    # replacing STR with your string or datatype to loop
    #need to ord the letter to be able to XOR it then reconver it back to a char to print it out nicely
    for i in tempString:
       finalString=finalString+chr(ord(i)^key)
    

    # Replace either the return or reassign your unencrypted string to finalString
    file.close()
    return finalString

studentSTR = studentCode()

print studentSTR

