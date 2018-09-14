"""
CPT Kyle Yoder
Lab2H grade calculator
06 Sept 2018
"""


studentDict={}
another =1

while(another !='0'):
    #get the students name and grade
    student=raw_input("Please enter a students name: \n")
    grade=int(raw_input("Please enter that students grade: \n"))

    #add the student and thier grade to the map
    studentDict[student]=grade
    
    #sort the map by highest grade to lowest
    names=sorted(studentDict.items(), key = lambda x: x[1], reverse=True)

    #loop through and print students and grades in order, then get total grades
    counter=0
    average=0
    for r in range(len(names)):
        print "{}: {}".format(names[r][0], names[r][1])
        average=average+names[r][1]
        counter+=1
    average=average/counter   
    #divide by total number of students to get average
    print "The class average is: {}".format(average)
    #check if they wish to enter more students
    another=raw_input("To enter another student enter 1 to stop enter 0 \n")
 
  

