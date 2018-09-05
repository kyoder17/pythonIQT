"""
CPT Kyle Yoder
lab2c tax calculator
04 Sept 2018
"""

"""
bannana=5
apple=6
tax=.07

print "Apples cost ${}".format(apple)
print "Bannans cost ${}".format(bannana)
print "Taxes are ${}".format(tax)

totalA=(apple+(apple*tax))
totalB=(bannana+(bannana*tax))
sale=(2*bannana)
sale+=(sale*tax)

print "The total for one apple is ${}".format(totalA)
print "The total for one bannana is ${}".format(totalB)
print "The total for 2 bannans is ${}".format(sale)
"""

#get the cost of the item

print (
"1: apples cost $5\n"
"2: bannans cost $7\n"
"3: bread cost $15\n"
)

#currently the item cost is hard coded
choice=int(input("Please enter the number of the item you would like to select"))


if (choice==1):
    item=5
elif(choice==2):
    item=7
elif(choice==3):
    item=15
else:
    print "No item selected taxes still applied"
    item=1
#current quantity is set at 4
quantity=input("How many of these would you like to buy")

purchase=item*quantity
#taxes are currently $0.07 on the dollar
tax=.0825
print "Taxes are ${}".format(tax)


# calculate price by adding the cost and the cost times taxes
itemTotal=purchase+(purchase*tax)
#print the total
print "The total cost of {} items at ${} each with tax is ${:0.2f}".format(quantity, item, itemTotal)